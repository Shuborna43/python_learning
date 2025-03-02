
# 1. Create a function called get_number_between(low, high). This function repeatedly asks the user to enter a number between low and high, and then returns the number when they do so. If they enter a number outside the low/high range, an error message is given and they are prompted again. Use the int() function to change user input from string to int, before comparing to numbers.

# Expected outcome:

# Enter a number between 11 and 38: 39
# Sorry, 39 is not in the range of 11 and 38!
# Enter a number between 11 and 38: 4
# ç
# Enter a number between 11 and 38: 20
# Thanks. 20 is in the range of 11 and 38!

#### can we do it by try and except function?


# user_number = int(input("enter a number between 11 and 38:   "))

# if user_number<11:
#     print(f"Sorry, {user_number} is not in the range of 11 and 38!")

# elif user_number>38:
#     print(f"Sorry, {user_number} is not in the range of 11 and 38!")

# else:
#     print(f"Thanks. {user_number} is in the range of 11 and 38!")


# 2. Create a function called get_info(). This prompts the user for their first name, last name, and birth year. Then it prints that data in CSV and JSON formats like this:


# Expected outcome:

# First name? tiGEr
# Last name? WoODs
# Born? 1975

# CSV: "Tiger,Woods,1975"
# JSON:
# "[
# 	{
#     	"first_name": "Tiger",
#     	"last_name": "Woods",
#     	"year_born": 1975
# 	}
# ]"

first_name = input ("enter your First Name:   ")
last_name = input ("enter your Last Name:  ")
year_born = int (input ("enter the year you born:  "))

#CVS_1 = f"First Name? {first_name}\nLast name? {last_name}\n Born? {year_born}"
# CVS_2 = "First Name?", "%s"% (first_name)  
# CVS_3 = "Last Name?", "%s"%(last_name)  
# CVS_4 = "Born?", "%d"%(year_born)  

#print (CVS_1)
# print (f"{CVS_2}")
# print (f"{CVS_3}") 
# print (f"{CVS_4}")
# CVS_5 = "First Name?:", "%s","Last Name?:","%s","Born?:","%d"%(first_name, last_name, year_born)   
# print (CVS_5)



# JSON:
# "[
# 	{
#     	"first_name": "Tiger",
#     	"last_name": "Woods",
#     	"year_born": 1975
# 	}
# ]"

Json_format_1= '{ "first_name": "%s", "last_name": "%s", "Year Born": "%d"}' %(first_name, last_name, year_born)
print (Json_format_1)












