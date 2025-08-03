def send_Email(to, subject='No Subject',body=''):
    print('Sending Email to ',to)
    print('Subject:',subject)
    print('Body:',body)


send_Email("user@example.com",body="This is body")

print("--------------------------------------------")

def print_profile(**kwarg):
    for key,value in kwarg.items():
        print("Your",key,"is",value)

print_profile(name="Jhon",age=30,city="Pune")
print("--------------------------------------------")

#def update_profile():





#print("---------------------------------------------")

def sum_n(num):
    if num==0:
        return 0
    return num+sum_n(num-1)

print(sum_n(10))


print("--------------------------------------------")

def fact(num):
    if num==1:
        return 1
    return num*fact(num-1)

print(fact(5))