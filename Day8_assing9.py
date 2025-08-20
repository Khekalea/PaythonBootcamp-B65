# Write function to split bill among friends
def split_bill():
  total_amount=int(input('Enter total amount of Bill :'))
  number_of_friends=int(input('Enter number of friends :'))

  print(f"The total bill is ₹{total_amount}.")
  print(f"There are {number_of_friends} friends splitting the bill.")

  amount_per_person = total_amount / number_of_friends

  print(f"Each person should pay: ₹{amount_per_person}") 


split_bill()




