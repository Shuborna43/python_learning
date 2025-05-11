#\A: Returns a match if the specified characters are at the beginning of the string. 
#Example 1:
# import re 
# result= re.findall(r"\Athe", "the sun rises")
# print(result)

#\b : Returns a match where the speicified characters at the beginning or at the end of a word
#Example 1:
# import re
# result_1 = re.findall(r"\bpain", "paint the house pain") #will check the full string for match in the beginning of the word 
# result_2 = re.findall(r"aint\b", "paint the house aint" ) #will check the full string for match in the ending of the word  
# print(result_1, result_2)

#\B: returns a match where the specified characters are present, but not at the beginning or at the end of a word 
#Example 1:
# import re
# result_1 = re.findall(r"\Bain", "paint the house") #will check the full string for match in the beginning of the word 
# result_2 = re.findall(r"ain\B", "paint the house" ) #will check the full string for match in the ending of the word  
# print(result_1, result_2)

#\d: returns a match where the string contains digits (numbers from 0-9)
#Example-1
# import re
# result = re.findall(r"\d", "my mobile number is 028364827")
# print(result)

#\D: returns a match where the string doesn't contain digit
#Example-1
# import re
# result = re.findall(r"\D", "my mobile number is 028364827")
# print(result)

#\s: retuens a match where the string contains a white (space, tab, newline) character 
# Example-1
# import re
# result = re.findall(r"\s", "my mobile number \n is \t 028364827")
# print(result)

#\s: retuens a match where the string doesn't contain a white (space, tab, newline) character 
# Example-1
import re
result = re.findall(r"\S", "my mobile number \n is \t 028364827")
print(result)

#\w = returns a match where the string contains any word characters (characters from small letter a-Z, digits from 0-9 and the underscore character)
# Example-1
# import re
# result = re.findall(r"\w", "my mob_ile n-umber \n is \t 028364827")
# print(result)

#\W = returns a match where the string doesn't contain any word characters 
# Example-1
import re
result = re.findall(r"\W", "my mob_ile n-umber \n is \t 028364827")
print(result)

#\Z = returns a match if the specified characters are at the end of the string
# Example-1
# import re
# result = re.findall(r"Spain\Z", "I live in Spain")
# print(result)
# Example-2
# import re
# result = re.findall(r"Spain\Z", " Spain I live in Spain")
# print(result)