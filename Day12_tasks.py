def enter_marks():
    try:
        marks= int(input('Enter students marks(0-100) :'))
        if marks <0 or marks>100:
             raise ValueError("Marks should be brtween 0 and 100")
        print('Marks Entered :',marks)
    except ValueError as e:
        print('Invalid input',e)
    finally:
        print('Entry process completed..')

enter_marks()

print('---------------TASK2-----------------')

def atm_bal():
     try:
        balance=5000
        amount=float(input('Enter amount to withraw :'))

        if amount <=0 :
            raise ValueError("Insfficient balance")
        
        balance -= amount
        print('Withrawal Sucessful...')
        print('Remaining Balance :',balance)

     except ValueError as e:
         print('Error',e)

     finally:
         print("Thank you for using ATM !!")
    

atm_bal()

print('--------------------Task3------------------')

