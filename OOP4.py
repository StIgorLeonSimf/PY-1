"""Множественное наследование, статические атрибуты"""
from OOP3 import Person


class MixinPlay:
    @staticmethod
    def play(channal=1):
        match channal:
            case 1:
                print('Звучит "Beatles ')
            case 2:
                print('Звучит "ABBA ')
            case 3:
                print('Звучит "Leps"')
            case 4:
                print('Звучит "Новостной канал"')
            case 5:
                print('Звучит "Концерт Игоря Крутого')


class Car(MixinPlay):
    name = 'Автомобиль'

    def ride(self):
        print(f'Как {Car.name} Едет по дороге')

    # @staticmethod
    # def play():
    #     print('звучит "Beatles"')


class Boat(MixinPlay):
    def swim(self):
        print('Ходит по воде')

    # @staticmethod
    # def play():
    #     print('звучит "ABBA"')


class Amphibian(Car, Boat):
    def display(self):
        print('Амфибия:')


# car = Car()
# boat = Boat()
# car.ride()
# boat.swim()
am = Amphibian()
am.display()
am.ride()
am.swim()
# print(isinstance(am, Car))
# print(isinstance(am, Boat))
# print(isinstance(am, Amphibian))
am.play(5)


class A:
    pass
    # def display(self):
    #     print('A')


class B(A):
    pass
    # def display(self):
    #     print('B')


class C(A):
    pass
    # def display(self):
    #     print('C')


class D(B, C, Person):
    def __init__(self, name='Marpha', age=19):
        Person.__init__(self,name, age)

    # def display(self):
    #     print('D')


print(D.mro())
obj = D()
obj.display()
print(obj)

class Name:
    def __init__(self, name):
        self.name = name

class Age:
    def __init__(self, age):
        self.age = age

class Human(Name, Age):
    def __init__(self, name, age):
        super().__init__(name)
        Age.__init__(self, age)

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def __repr__(self):
        return f'{self.name} - {self.age} '

h = Human('Harry', 19)
h1 = Human('John', 23)
print(h)
humans = [h, h1]
print(humans)