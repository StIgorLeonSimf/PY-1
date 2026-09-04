"""Абстрактные классы."""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calk_square(self):
        pass

    def display(self):
        print(self.name)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__('Круг')
        self.radius = radius

    def calk_square(self):
        return math.pi * self.radius ** 2

    def display(self):
        super().display()
        print(f'Радиус: {self.radius} ед.\n'
              f'Площадь: {self.calk_square():.2f} кв.ед')


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__('Прямоугольник')
        self.width = width
        self.height = height

    def calk_square(self):
        return self.width * self.height

    def display(self):
        super().display()
        print(f'Ширина: {self.width} ед.\n'
              f'Высота: {self.height} ед.\n'
              f'Площадь: {self.calk_square()} ед.')


# class Gadget(ABC):
#     @abstractmethod
#     def display(self):
#         pass
#
#     @abstractmethod
#     def talk(self):
#         pass
#
#     @abstractmethod
#     def inet(self):
#         pass


# class Smartphone(Gadget):
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print('Обеспечивает разговор')
#
#     def inet(self):
#         print('Обеспечивает передачу данных')
#
#     def display(self):
#         print('Обеспечивает отображение данных')
#
#
# class Telephone(Gadget):
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print('Обеспечивает разговор')
#
#     def inet(self):
#         pass
#
#     def display(self):
#         pass

class Talk(ABC):
    @abstractmethod
    def talk(self):
        pass

class Inet(ABC):
    @abstractmethod
    def inet(self):
        pass

class Display(ABC):
    @abstractmethod
    def display(self):
        pass

class Smartphone(Talk, Inet, Display):
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('Обеспечивает разговор')

    def inet(self):
        print('Обеспечивает передачу данных')

    def display(self):
        print('Обеспечивает отображение данных')

class Telephone(Talk):
    def talk(self):
        print('Обеспечивает разговор')


if __name__ == '__main__':
    pass
    # c = Circle(2)
    # c.display()
    # rect = Rectangle(4, 5)
    # rect.display()