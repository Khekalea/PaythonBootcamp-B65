def counter():
   # global count 
    count=0
    def increment():
        nonlocal count
        count=count+1
        return count
    return increment
c=counter()
print(c())
print(c())