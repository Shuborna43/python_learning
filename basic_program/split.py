#string methods: split()

# split_1 = "I love Python"
# split_2 = "I love Python"


# token_1 = split_1.split(" ")
# token_2 = split_2.split("o") #delimeter


# print(token_1)
# print(token_2)

#string method: join()

# token_1 = ["I", "love", "Python"]
# join_1 = " ".join(token_1)

# print(join_1)

# path_tokens = ["desktop", "Python", "Session2.doc"] 
# file_path = "/".join(path_tokens)

# print(file_path)

#More string built-in method 

# replace(old, new)

replace_1 = "Hello World World" 
new_1 = replace_1.replace("World","Python")
print(new_1)

# replace(old, new, count)
replace_2 = "Hello World World World" 
new_2 = replace_2.replace("World","Python",1)

# find(x)
find_1 = replace_2.find("World")

# find(x, start), if find doesn't get the value it will return "-1" as output
find_2 = replace_2.find("W",7)

# find(x, start, end), if find doesn't get the value it will return "-1" as output
find_3 = replace_2.find("W",7,10)
find_4 = replace_2.find("W",7,13)

# rfind(x)
find_5 = replace_2.rfind("World")

# count(x) #counts the existence of the word
count_1 = replace_2.count("World")

print(new_2,find_1,find_2,find_3,find_4,find_5,count_1)

# isalnum()
s1 = "  pyTHon123  " #leading white space, trailing white space- the spaces before and after
print(s1.isalnum())

# isdigit()
print(s1.isdigit())

# islower()
print(s1.islower())

# isupper()
print(s1.isupper())

# isspace()
print(s1.isspace())

# startswith()
print(s1.startswith("P"))

# endswith()
print(s1.endswith("P"))

# capitalize() #makes/converts the first letter
print(s1.capitalize())

# lower() #makes all characters lowercase
print(s1.lower()) 

# upper()#makes all characters uppercase
print(s1.upper())

# strip(), it will delete the lead and trailing spaces
print(s1.strip())

# title(), it will convert each first char of each word into uppercase
title_1 = "hello world from python"
print(title_1.title())







