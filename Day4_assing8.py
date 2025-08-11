age=int(input("Enter your AGE :"))
citizen=input('Enter yes/no if you are Citizen :')

print('AGE is :',age)
print('Citizen yes/no :',citizen)

if age>=18 and citizen=='yes':
    print('Candidate is eligible for vote :')
else:
    print('Candidte is not eligible for vote :')