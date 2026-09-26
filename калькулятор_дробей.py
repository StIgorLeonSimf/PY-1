import math
from tkinter import *
from tkinter import messagebox as mb

def validation_func_num(vidjet):
    text = vidjet.get().strip()
    corr_text = ''.join(symbl for symbl in text if symbl in "123456789")
    if corr_text != text:
        mb.showerror('Ошибка ввода', f'Символ не разрешен')
        vidjet.delete(0, 'end')
        vidjet.insert(0, corr_text)


def validation_func_oper(vidjet):
    text = vidjet.get().strip()
    corr_text = ''.join(symbl for symbl in text if symbl in "+-/*")
    if corr_text != text:
        vidjet.delete(0, 'end')
        vidjet.insert(0, corr_text)


def add(n1,d1, n2, d2):
    n = n1 * d2 + n2 * d1
    d = d1 * d2
    return n, d


def sub(n1,d1, n2, d2):
    n = n1 * d2 - n2 * d1
    d = d1 * d2
    return n, d


def mult(n1,d1, n2, d2):
    n = n1 * n2
    d = d1 * d2
    return n, d


def div(n1,d1, n2, d2):
    if d1 == 0 or d2 == 0:
        raise ZeroDivisionError('division by zero')
    n = n1 * d2
    d = d1 * n2
    return n, d


def calk():
    try:
        n1 = int(num1.get())
        d1 = int(den1.get())
        n2 = int(num2.get())
        d2 = int(den2.get())
        operator = oper.get().strip()
        res = (0, 1)
        match operator:
            case '+': res = add(n1,d1, n2, d2)
            case '-': res = sub(n1,d1, n2, d2)
            case '*': res = mult(n1,d1, n2, d2)
            case '/': res = div(n1,d1, n2, d2)

        nod = math.gcd(res[0], res[1])

        n = int(res[0] / nod)
        d = int(res[1] / nod)
        int_p = ''
        if n > d:
            int_p = n // d
            n = n % d
        if n == 0:
            n = ''
            d = ''

        if n == d and int_p=='':
            n = ''
            d = ''
            int_p = 1

        int_part.config(text=int_p)
        num3.config(text=n)
        den3.config(text=d)

    except Exception:
        pass


if __name__ == '__main__':

    root = Tk()
    WIDTH = root.winfo_screenwidth()
    HEIGHT = root.winfo_screenheight()
    X = 300
    Y = 140
    root.geometry(f"{X}x{Y}+{WIDTH // 2 - X // 2}"
                  f"+{HEIGHT // 2 - Y // 2 - 20}")
    root.title('Калькулятор дробей')
    frame = Frame(root)
    frame.pack(pady=10)

    num1 = Entry(frame, width=2)
    num1.config(font='Arial 15', justify='center')
    num1.grid(row=0, column=0)
    line1 = Label(frame, text=chr(8212)*3)
    line1.grid(row=1, column=0)
    den1 = Entry(frame, width=2)
    den1.config(font='Arial 15', justify='center')
    den1.grid(row=2, column=0)

    oper = Entry(frame, font='Arial 15')
    oper.config(width=2, justify='center')
    oper.grid(row=1, column=1, padx=5)

    num2 = Entry(frame, width=2)
    num2.config(font='Arial 15', justify='center')
    num2.grid(row=0, column=2)
    line2 = Label(frame, text=chr(8212)*3)
    line2.grid(row=1, column=2)
    den2 = Entry(frame, width=2)
    den2.config(font='Arial 15', justify='center')
    den2.grid(row=2, column=2)

    btn = Button(frame, text='=', width=2, font='Arial 15', command=calk)
    btn.grid(row=1, column=3, padx=5)

    int_part = Label(frame, text='  ', bg='light gray')
    int_part.config(font='Arial 20', width=2, justify='center')
    int_part.grid(row=1, column=4)

    num3 = Label(frame, width=2, bg='light gray')
    num3.config(font='Arial 15', justify='center')
    num3.grid(row=0, column=5)
    line3 = Label(frame, text=chr(8212)*3)
    line3.grid(row=1, column=5)
    den3 = Label(frame, width=2, bg='light gray')
    den3.config(font='Arial 15', justify='center')
    den3.grid(row=2, column=5)

    # num1.bind('<KeyRelease>', lambda event: validation_func_num(num1))
    # den1.bind('<KeyRelease>', lambda event: validation_func_num(den1))
    # num2.bind('<KeyRelease>', lambda event: validation_func_num(num2))
    # den2.bind('<KeyRelease>', lambda event: validation_func_num(den2))

    vidjets = (num1, den1, num2, den2)
    for v in vidjets:
        v.bind('<KeyRelease>', lambda event, w=v: validation_func_num(w))
    oper.bind('<KeyRelease>', lambda event: validation_func_oper(oper))

    root.mainloop()