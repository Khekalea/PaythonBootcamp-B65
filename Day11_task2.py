attempts=0

def login():
   global attempts
   attempts = attempts+1
   print("Login attempt",attempts)

   login()
   
   login()