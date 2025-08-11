def greet():
    name='ShriHari'
    print("Hello",name)

greet()

print('----------------------------------')

name='Amit'
def greetOne():
    print('Hello',name)

greetOne()

print('----------------------------------')

count=0
def counter():
    global count
    count=count+1

print('Before function call',count)
counter()
print('After function call',count)
counter()
print('After1 function call',count)
counter()
print('After2 function call',count)
def counterDecrement():
    global count
    count=count-1

counterDecrement()
print('After Decrement',count)
counter()
print('After3 function call',count)


