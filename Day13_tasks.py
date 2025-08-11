
class ClassName:
    pass
print("--------------------TASK1-----------------")

class Car:
    def __init__(self,color,brand):
        self.color= color
        self.brand= brand

    def getProperties(self):
        print("COlor of car is :",self.color)
        print("Brand of car is:",self.brand)

    def start(self):
        print('Car Started..')
    
    def stop(self):
        print('By using break')

    
    
c=Car('Red','Maruti')

print(c.start(),'Alto')
print(c.getProperties(),'Alto')

c1=Car('Black','Ford')
print(c1.start(),'Ford')
print(c1.getProperties(),'Ford')

c2=Car('Blue','Porsche')
print(c2.start(),'Porsche')
print(c2.getProperties(),'Porsche')
print('To stop a car you have to use break :',c2.stop())

print("--------------------TASK2-----------------")

class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getInfo(self):
        print(self.name, ':::',self.age)

s=Student('ABC',20)
s1=Student('XYZ',15)

print("Name of student 1:",s.getInfo())
print('Name of student 2:',s1.getInfo())

print("--------------------TASK3-----------------")

class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def display(self):
        print('Owner :',self.owner,'Balance:',self.balance)
        
b=BankAccount('Abc',5000)
print('Name of owner and Balance is:',b.display())

print("--------------------TASK3-----------------")

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def details(self):
        print("Name :",self.title,", Author:",self.author)

b=Book('Mahabharat','Ved Vyas')
print("Book Details are",b.details())        
