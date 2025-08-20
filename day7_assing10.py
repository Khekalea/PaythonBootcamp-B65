menu = ['pizza', 'Burger', 'pasta', 'salad']

for item_number, food_item in enumerate(menu):

  print(f"{item_number + 1}. {food_item}")

print("\n")

user_choice = input("Please enter the number of the item you would like to order: ")
print(f"You chose menu item number : {user_choice}!")