# the [square brakets] indicates list, ranges and/or list of ranges. means range between unless- is the first or last character in the braket[]. braket[] indicates one character. 
#1. [arn]: returns a match where one of the specified characters (a,r,n) present. 
# #Example: list
# import re
# result = re.findall(r"[arn]", "journey by train")
# print(result)

#Example: range [1-9]
# import re
# result = re.findall(r"[1-9]", "journey by train 78654")
# print(result)

# #Example: any lowercase character range [a-n] 
# import re
# result = re.findall(r"[a-n]", "journey by train 78654")
# print(result)

# #Example: any upper case character range [A-N] 
# import re
# result = re.findall(r"[A-N]", "Journey By Train 78654") #case sensitive 
# print(result)

#[^arn] = retiurns a match for any character except a, r, n
# #Example: 
# import re
# result = re.findall(r"[^arn]", "Journey By TraiN 78654") #case sensitive
# print(result)

#[0123]: returns a match where any of the specified digits are present 
# import re
# result = re.findall(r"[012386]", "Journey By TraiN 78654") 
# print(result)

#[0-5][0-9]: returns a match for any two digit number from 00 and 59
#example 
# import re
# result = re.findall(r"[0-9][0-9]", "now time is 09:53")#considers only two digit numbers
# print(result)

#[a-zA-Z]: returns a match for any character alphabetically between a-z, lowercase or upper case 
# import re
# result = re.findall(r"[a-zA-Z]", "I Have a Doll")
# print (result)

# #[a-zA-Z]: returns a match for any character alphabetically between a-z, lowercase or upper case 
# import re
# result = re.findall(r"[a-zA-Z]", "I Have a Doll")
# print (result)

#[+]: in sets, +,*,.,|,(),{},$ has no special meaning, so [+] means return a match for any + character in the string 
#Example
import re
result = re.findall(r"[or+]", "I have three cats +") # + is considered as a character
print(result)