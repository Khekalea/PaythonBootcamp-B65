# Write function that calculates simple interest
def calculate_simple_interest(principal, rate, time):
  
  interest = principal * rate * time
  
  return interest

principal_amount = 1000
interest_rate = 0.05
loan_time = 2

total_interest = calculate_simple_interest(principal_amount, interest_rate, loan_time)


print(f"The simple interest on a loan of ₹{principal_amount} at a rate of {interest_rate*100}% for {loan_time} years is: ₹{total_interest}")