from typing import Union, Optional, List, Dict


class Person:
    def __init__(self, name, age):
        self.__name: str = name
        self.__age: int = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return f'{self.__name} - {self.__age}'


class Flat:
    """Класс описывающий квартиру."""
    def __init__(self, number):
        self.__number: int = number
        self.__persons: List[Person] = []

    @property
    def number(self):
        return self.__number

    @property
    def persons(self):
        return self.__persons

    def add_person(self, *persons: Person) -> None:
        for person in persons:
            if not isinstance(person, Person):
                raise TypeError('Объект не является экземпляром класса "Persone"')
            self.__persons.append(person)

    def display(self):
        max_name = max(self.__persons, key=lambda x: len(x.name))
        mx = len(max_name.name)

        print(self)
        for i, person in enumerate(self.__persons, 1):
            print(f'\t\t\t{i}. {person.name:{mx}} - {person.age}')

    def __str__(self):
        return (f'\t\tКвартира: №{self.__number} ')


class Floor:
    """Класс описывающий этаж."""
    def __init__(self, numb):
        self.__numb: int = numb
        self.__flats: List[Flat] = []

    @property
    def flats(self):
        return self.__flats

    @property
    def numb(self):
        return self.__numb

    def add_flats(self, *flats: Flat) -> None:
        for flat in flats:
            if not isinstance(flat, Flat):
                raise TypeError('Объект должен быть экземпляром класса "Flat"')
            if flat.number > 999:
                raise ValueError('Номер не может быть больше 3-х знаков')
            self.__flats.append(flat)

    def display(self):
        # names = []
        # for flat in self.__flats:
        #     for person in flat.persons:
        #         names.append(person.name)

        name_max = max((person.name for flat in self.__flats
                        for person in flat.persons), key=lambda x: len(x))
        mx = len(name_max)
        print(self)
        count = 1
        for flat in self.__flats:
            print(flat)
            for person in flat.persons:
                print(f'\t\t\t{count:3}. {person.name:{mx}} - {person.age}')
                count += 1
    def __str__(self):
        return f'\tЭтаж №{self.__numb}: Кол-во квартир: - {len(self.__flats)}.'


class Dom:
    """Класс описывающий дом."""
    def __init__(self, num):
        self.__num: int = num
        self.__floors: List[Floor] = []

    @property
    def flats(self):
        return self.__flats

    @property
    def num(self):
        return self.__num

    def add_floors(self, *floors: Floor) -> None:
        for floor in floors:
            if not isinstance(floor, Floor):
                raise TypeError('Объект должен быть экземпляром класса "Floor"')
            if not isinstance(floor.numb, int):
                raise TypeError('Номер этажа должен быть числом')
            self.__floors.append(floor)

    def display(self):
        name_max = max((person.name for floor in self.__floors
                        for flat in floor.flats
                        for person in flat.persons), key=lambda x: len(x))
        mx = len(name_max)
        print(self)
        count = 1
        for floor in self.__floors:
            print()
            print(floor)
            for flat in floor.flats:
                print(flat)
                for person in flat.persons:
                    print(f'\t\t\t{count:3}. {person.name:{mx}} - {person.age}')
                    count += 1


    def __str__(self):
       return f'Дом №{self.__num}'






p1 = Person('John Lenon', 33)
p2 = Person('Pol Mackartney', 43)
p3 = Person('Klava Koka', 30)
p4 = Person('Said Abdurahman ibn Hattab', 80)
p5 = Person('Ny', 12)
p6 = Person('John Lenon', 33)
p7 = Person('Pol Mackartney', 43)
p8 = Person('Klava Koka', 30)
p9 = Person('Said Abdurahman ibn Hattab', 80)
p10 = Person('Ny', 12)

kv45 = Flat(45)
kv46 = Flat(46)
kv47 = Flat(47)
kv48 = Flat(48)
kv45.add_person(p1, p2)
kv46.add_person(p3, p4, p5)
kv47.add_person(p6, p7, p10)
kv48.add_person(p8, p9)
# kv45.display()
# kv46.display()
# print(Flat.__doc__)
f4 = Floor(4)
f4.add_flats(kv45, kv46, kv47, kv48)
# f4.display()

dom = Dom(25)
f5 = Floor(5)
p11 = Person('John Lenon', 33)
p12 = Person('Pol Mackartney', 43)
p13 = Person('Klava Koka', 30)
p14 = Person('Said Abdurahman ibn Hattab', 80)
p15 = Person('Ny', 12)
p16 = Person('John Lenon', 33)
p17 = Person('Pol Mackartney', 43)
p18 = Person('Klava Koka', 30)
p19 = Person('Said Abdurahman ibn Hattab', 80)
p20 = Person('Ny', 12)

kv55 = Flat(55)
kv56 = Flat(56)
kv57 = Flat(57)
kv58 = Flat(58)
kv55.add_person(p11, p12)
kv56.add_person(p13, p14, p15)
kv57.add_person(p16, p17, p18)
kv58.add_person(p19, p20)
f5.add_flats(kv55, kv56, kv57, kv58)
dom.add_floors(f4, f5)
dom.display()

