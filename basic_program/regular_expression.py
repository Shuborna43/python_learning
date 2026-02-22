# Regular Expression: 
# 1. Regular expressions are very commonly used throughout computer programming. 
# 2. Regular expressions are strings. In particular, our regex will be simpler if we use raw strings like; r" ". 
# 3. Regular expressions are used for pattern matching in other strings. Patterns can be created, found, replaced and much more. 
# Example: Does it match the pattern of an email address, postal code, or a phone number. 

#re object/ re module and its methods: 
# 1. To use regular expressions in python, we must import re. 
# 2. The re object has methods such as; 
# match(): checks if the pattern exists at the beginning of the string.  
# search(): searches for the pattern throughout the entire string. It returns a match object from the first position where the pattern matches.  
# split(): Splits the string based on the pattern.  
# findall(): creates a list of all parts that match the pattern.   
# finditer(): returns an iterator of all parts that match the pattern.  
# sub(): replaces the matched pattern with something else. 

# The order for parameters in python is generally needle (What to search), haystack (where to look for or search). 

# Match(): It only searches from the begining of the string. If the pattern matches at the start, it returns the match which contains [1. the position where the match starts, 2. the position where the match ends, 3. the exact part of the string that matched]. If there is no match it returns none. 
# Example 1: 
# import re

# string_1 = "Hello world"
# pattern_1 = r"Hello"     

# result_1 = re.match(pattern_1, string_1)

# if result_1:
#     print("match found:", result_1.group())
#     print("starts at:", result_1.start(), "ends at:", result_1.end())
# else:
#     print("No match found")

#Example 2:
# import re

# string_2 = "Hello world"
# pattern_2 = r"world"

# result_2 = re.match(pattern_2, string_2)

# # if result_2:
# #     print("match found:", result_2.group())
# # else:
# #     print ("match not found")

# print(result_2)

#search(): It searches throughout the entire string. It returns a match object from the first position where the pattern matches. 
#example 1:
# import re

# string_3 = "Hello Worlds Hello"
# pattern_3 = "llo"

# result_3 = re.search(pattern_3, string_3)

# if result_3:
#     print("match found:", result_3.group())
#     print("starts at:", result_3.start(), "ends at:", result_3.end())
# else:
#     print("No match found")


#example 2:
# import re

# string_3 = "Hello Worlds Hello"
# pattern_3 = "ggg"

# result_3 = re.search(pattern_3, string_3)

# if result_3:
#     print("match found:", result_3.group())
#     print("starts at:", result_3.start(), "ends at:", result_3.end())
# else:
#     print("No match found")

#findall(): findall() uses regular expression to search for a specific pattern throughout the entire string and returns all the matches as a list. If one or more matches are found it returns all of them in a list. If no matches are found, it returns an empty list [], not none. 
# # Example 1:
# import re

# string = "it is British Columbia"
# pattern = r"i[ts]"

# result = re.findall(pattern, string)

# print(result)

# Example 2:
# import re

# string = "it is British Columbia"
# pattern = r"i[bc]"

# result = re.findall(pattern, string)

# print(result)

# finditer(): The finditer() method creates a match object for each match throughout the entire string based on the regular expression pattern, and returns them as an iterator. each match obeject contains:
# the part of the string that matched (group())
# where the match starts (start())
# where the match ends (end())
# 
#Example 1:
# import re

# string = "cat bat rat hat mat water"
# pattern = r"\b\w{3}\b" #w{3}=words only with 3 letters, #\b helps make sure the match starts and ends at a word boundary. 

# matches = re.finditer(pattern, string)
# for match in matches:
#     print("matched text", match.group())
#     print("starts at", match.start(),"ends at", match.end())
#     print ("...")
#     #print(match)

# #Example 2:
# import re

# string = "cat bat rat hat mat water"
# pattern = r"\w{3}" #w{3}=will return only matched 3 letters

# matches = re.finditer(pattern, string)
# for match in matches:
#     print("matched text", match.group())
#     print("starts at", match.start(),"ends at", match.end())
#     print ("...")
#     #print(match)

#sub(): sub() in python is used to search and replace parts of a string that match a regular expression pattern. Syntax:
# re.sub(pattern,replacement,string) 

# #Example 1:
# import re

# text = "my phone number is 017-151-58686"
# pattern = r"\d"
# replacement = "*"
# result = re.sub(pattern, replacement, text)
# print (result) 

# #Example 2:
# import re

# text = "my phone number is 017-151-58686"
# result = re.sub(r"\d", "*", text)
# print (result) 