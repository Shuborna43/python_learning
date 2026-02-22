#set[a-m]: one of the charater in the set
#Example 1:
# import re
# result = re.findall("[a-m]", "hello magic")
# print (result)

#\: signals a special sequence (can also be used to escape special characters)
#Example 1:
# import re
# result = re.findall(r"\d", "order 66 and 501st") #d-find digits 
# print (result)

#.: any single character except new line character 
#Example:
# import re
# result = re.findall(r"he..o", "hello hero help hezzo")
# print (result)

#^: starts with
#Example:
# import re
# result = re.findall(r"^hello", "hello world")
# print(result)

#$: end with
#Example:
# import re 
# result = re.findall(r"world$", "hello world")
# print(result)

#*: zero or more ocurrences 
# import re
# result = re.findall(r"ai*", "paint aiii aim")
# print(result)

#+: 1 or more occurence
# import re
# result = re.findall(r"ai+", "it is")
# print(result)

#{}: exactly the specified number of occurences 
# import re 
# result = re.findall(r"a{2}", "aa aaaa aba")#{2} =indicating to double a
# print(result)

#|: either or
# import re
# result = re.findall(r"fall|stay", "I will fall but you stay")
# print(result)

#(): capture and group 
# import re
# result = re.search(r"(ab)+", "abababc")
# print(result)

# #?: optional
import re
result = re.findall(r"ab?c", "abc bc ac ab") #a and c must be there 
print(result)
