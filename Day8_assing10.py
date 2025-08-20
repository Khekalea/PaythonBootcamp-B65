# Create function that converts Hours in Minuts and seconds
def convert_hours(hours):

  minutes = hours * 60  

  seconds = hours * 3600
  
  return minutes, seconds

hours_to_convert = int(input('Enter Hours to convert :'))

total_minutes, total_seconds = convert_hours(hours_to_convert)

print(f"{hours_to_convert} hours is equal to:")
print(f"- {total_minutes} minutes")
print(f"- {total_seconds} seconds")