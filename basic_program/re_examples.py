strings = ("abcdefg",
           "aeiou",
           "AEIOU",
            "a1b2c3d4",
            "a12b34c56",
            "jason_harrison@bcit.ca",
            "bcit",
            "2012-02-29",
            "BCIT SFU UBC MIT",
            "a@b.com",
            "$123.45",
            "$67.78.33",
            "1999-12-25",
            "$111.222",
            "x@d..com",
            "5'11\"",
            "2020-01-31",
            "6'12\"",
            "-5'9\"",
            "grrrrrrrrrrrrrrrr",
            "aaaeeeeeeeiiiiiii",
             "aaaeeeeeeeiiiiiii!",
            "jason,harrison,bcit,45",
            "tiger,woods,golfer,100",
            "shaquille,o'neal,basketball,101"
            )

#solution-1: 

# for string in strings:
#   if "a" in string.lower():
#     print(string, "has a")
#   else:
#     print(string, "has no a")

#solution-2: 
# import re
# for string in strings:  
#     if re.findall(r"a",string.lower()):
#         print(string, "has a")
#     else:
#         print(string, "has no a")

#solution-3: 
# import re
# for string in strings:  
#     if re.findall(r"a",string,re.IGNORECASE):
#         print(string, "has a")
#     else:
#         print(string, "has no a")


#solution-4: 
# import re
# for string in strings:  
#     if re.findall(r"a",string,re.IGNORECASE):
#         print(string, "has a")
#     else:
#         print(string, "has no a")


#solution-5:

# import re
# i = 0
# while i < len(strings):
#     string = strings[i]
#     if re.findall(r"ab|bc",string,re.IGNORECASE):
#       print(f"{string} contains ab or bc")
#     else:
#       print(f"{string} doesn't contain ab or bc")
#     i+=1



            