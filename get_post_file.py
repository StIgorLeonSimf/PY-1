from tkinter import *
from tkinter import filedialog as fd, messagebox as mb
from tkinter import (Toplevel, Listbox,
                     Scrollbar, HORIZONTAL, VERTICAL)
from tkinter import ttk


import requests
import pyperclip
import os
import json



def save_history(file_path, download_link, history_file='test_upload_history.json'):
    history = []
    print(history_file)
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            history = json.load(f)
    history.append({'file_name':os.path.basename(file_path), 'download_link': download_link})
    with open(history_file, 'w') as f:
        json.dump(history, f, indent=4)


def show_history():
    if not os.path.exists(history_file):
        mb.showinfo('History', 'История загрузок пуста.')
        return
    history_wind = Toplevel(root)
    history_wind.title('History downloads')

    files_listbox = Listbox(history_wind, width=50, height=20)
    files_listbox.grid(row=0, column=0, pady=10, padx=(10, 0))
    links_listbox = Listbox(history_wind, width=50, height=20)
    links_listbox.grid(row=0, column=1, pady=10, padx=(0, 10))
    with (open(history_file, 'r')) as f:
        history = json.load(f)
        for item in history:
            files_listbox.insert(END, item['file_name'])
            links_listbox.insert(END, item['download_link'])




def upload():
    try:
        filepath= fd.askopenfilename()
        if filepath:
            with open(filepath, 'rb') as f:
                files = {'file': f}
                response = requests.post('https://store1.gofile.io/uploadFile', files=files)
                response.raise_for_status()
                download_link = response.json().get('data').get('downloadPage')
                if download_link:
                    entry.delete(0, 'end')
                    entry.insert(0, download_link)
                    pyperclip.copy(download_link)
                    save_history(filepath, download_link, history_file)
                    mb.showinfo('Информация',
                                'Ссылка находится в буфере обмена ')
                else:
                    raise ValueError('Ссылка не получена!')
    except requests.RequestException as e:
        mb.showerror('Ошибка сети', f'Произошла ошибка {e}')
    except ValueError as e:
        mb.showerror('Ошибка', f'Произошла ошибка {e}')
    except Exception as err:
        mb.showerror('Ошибка', f'Произошла ошибка {err}')


if __name__ == '__main__':
    root = Tk()
    history_file = 'history.json'
    root = Tk()
    root.title('Сохранение файлов в облаке')
    root.geometry('400x200')
    upload_btn = ttk.Button(root, text='Загрузка файла', command=upload)
    upload_btn.pack(pady=20)

    entry = ttk.Entry(root, width=40)
    entry.pack()

    history_btn = ttk.Button(root,text='Показать историю', command=show_history)
    history_btn.pack(pady=10)

    root.mainloop()