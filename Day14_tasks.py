class Vehicle:
    def starrt(self):
        print('Car Starts...')
    
class Car(Vehicle):
    def play_music(self):
        print('Press play button on screen..')

c=Car()
c.starrt()
c.play_music()

print('-----------------TASK2(Inheritance)------------------')

class Animal:
    def animal_sound(animal):
        # print('Animal can speak..')
        animal.sound()
class Dog(Animal):
    def sound(self):
        print('Dog Barks....')
class Cat(Animal):
    def sound(self):
        print('Cat Mew...')

o=[Dog(),Cat()]
for animal in o:
    print(animal.sound())

print('-----------------TASK3(Inheritance)------------------')

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def fullName(self):
        print('This is employees name...',self.name)
class Manager(Employee):
    def baseSalary(self):
        print('This is base salary...',self.salary)

m=Manager('Jhon',50000)
m.fullName()
m.baseSalary()

print('-----------------TASK4(Polymorphism)------------------')

class Vehicle:
    def drive(self):
        return "moving"
class Car(Vehicle):
    def drive(self):
        return "Driving"
class Bike(Vehicle):
    def drive(self):
        return "Ride"
    
Honda=Car()
Ducati=Bike()

print("Honda :",Honda.drive())
print("Ducati :",Ducati.drive())

print('-----------------TASK5(Encapsulation)------------------')

class Person:
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setNewName(self,newName):
        self.name=newName
        return self.name
    
Jhon=Person('Jhon Doe')

print(Jhon.getName(),'Created...')
Jhon.setNewName('Jhonnnn Doeeee')
print(Jhon.getName(),'After Cahnge...')

print('-----------------TASK6(Encapsulation)------------------')

class BankAccount:
    def __init__(self):
        self.__balance=0
    def deposite(self,amt):
        self.__balance+=amt
    def checkbalance(self):
        return self.__balance

b=BankAccount()
print(b.checkbalance(),'Before deposite/First time...')

b.deposite(10000)
print(b.checkbalance(),'After Deposite....')

print('-----------------TASK7(Abstraction)------------------')

from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class Car(Vehicle):
    def strt_engine(self):
        print('Engin Started...')
m=Car()
m.start_engine()

print('-----------------TASK8(Encapsulation)------------------')

from abc import ABC , abstractmethod

class Animal(ABC):
    def 

