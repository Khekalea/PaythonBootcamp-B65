# Write a function to convert Celsius into Fahrenheit
def c_To_f(celsius):
  
 
  fahrenheit = (celsius * 9/5) + 32

  return fahrenheit


celsius_temp = 25


fahrenheit_temp = c_To_f(celsius_temp)


print(f"{celsius_temp} degrees Celsius is equal to {fahrenheit_temp} degrees Fahrenheit.")