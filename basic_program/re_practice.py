#problem-1: A postal code alternates between letters and digits, 6 characters total, with an optional space after the first three characters. 

#solution:1 (match)
# string = "V7N 2M2"
# import re

# if re.match(r"^[A-Z][0-9][A-Z] ?[0-9][A-Z][0-9]$",string):
#     print (f"{string} is correct")
# else:
#     print (f"{string} is incorrect")

#solution-2 (search)
# string = "V7N 2M2"
# import re

# if re.search(r"^[A-Z][0-9][A-Z] ?[0-9][A-Z][0-9]$",string):
#     print (f"{string} is correct")
# else:
#     print (f"{string} is incorrect")

#solution-3 (alternative pattern)

# import re
# string = "V7N 2M2"
# if re.search(r"^[A-Z]\d[A-Z] ?\d[A-Z]\d$",string):
#     print (f"{string} is a valid postal code")
# else:
#     print (f"{string} is an invalid postal code")



#problem-2: A phone number can be either:
#  - ten digits in a row  e.g. 6045551212
#  - three digits, space, three digits, space, four digits  e.g. 604 555 1212
#  - three digits, hyphen, three digits, hyphen, four digits  e.g. 604-555-1212
# - three digits surrounded by (parentheses), space or not, three digits,  e.g. (604)555 1212
# space, four digits  e.g. (604) 555 1212

#solution-1
# import re
# cell_no = "6045551212"
# if re.search(r"^\d{10}$|^\d{3} ?\d{3} ?\d{4}$|^\d{3}-?\d{3}-?\d{4}$|^\(\d{3}\) ?\d{3} ?\d{4}$", cell_no):
#     print (f"{cell_no} is accepted")
# else:
#     print (f"{cell_no} is not accepted")




#solution-2
import re
cell_no = "(604) 555 1212"
if re.match(r"^\d{10}$|^\d{3} ?\d{3} ?\d{4}$|^\d{3}-?\d{3}-?\d{4}$|^\(\d{3}\) ?\d{3} ?\d{4}$", cell_no):
    print (f"{cell_no} is accepted")
else:
    print (f"{cell_no} is not accepted")


