def calculator(a,b,user_choice):
 if user_choice == "add":
  return a+b
 elif user_choice == "minus":
  return a-b
 elif user_choice == "mult":
  return a*b
 elif user_choice == "div":
  if b==0:
    return "zero error"
  else:
   return a/b
 else:
  return "please enter correct instruction"

user_choice = input('insert what you want to do---- add/minus/mult/div:')
a = int(input("insert value for a:   "))
b = int(input("insert value for b:   "))
result = calculator(a,b,user_choice)  
#print ("result of the", user_choice, "is", result) 
print(f"result of the {user_choice} is {result}")