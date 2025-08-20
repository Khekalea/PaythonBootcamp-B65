# Write a function calculate total price after tax
def calculate_total_price(price, tax_rate):
  
  
  tax_amount = price * tax_rate
  
  
  total_price = price + tax_amount
  

  return total_price


toy_price = 20.00
sales_tax = 0.08 


final_cost = calculate_total_price(toy_price, sales_tax)


print("The toy's original price is: ₹", toy_price)
print("The sales tax rate is: ", sales_tax)
print("The final price with tax is: ₹", final_cost)