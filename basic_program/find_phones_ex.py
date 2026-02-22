# You are given a block of text containing multiple phone numbers, each possibly separated by spaces or written as a continuous string.
# text = '''
# 604 123 2345
# 778 123 3456
# 604 456 5678
# 778 456 5678
# 60467867878
# 7781234578
# '''
# Write a Python function named find_phones_with_area_code(start, end, text) that takes the following arguments:

# 	start (int): the area code that the number must start with

# 	end (int): the last two digits that the number must end with

# 	text (str): the block of text in which to search for matching phone numbers

# Use Python's re module to build a regular expression that:

# 	Starts with the specified area code (start)

# 	May or may not contain a space after the area code

# 	Has 5 to 7 digits (or digits with spaces in between) after the area code

# 	Ends with the specified two-digit number (end)

# 	Matches entire lines only (not partial strings)

# Print the match objects using print(m) where m is each match returned by re.finditer().

# Enable multiline matching so that each line in text is evaluated separately.




import re
text = '''
604 123 2345
778 123 3456
604 456 5678
778 456 5678
60467867878
7781234578
'''

def find_phones_with_area_code(start, end, text):
    pattern = "^"+str(start)+" ?[0-9 ]{5,7}"+str(end)+"$"
    #pattern = "^"+str(start)+" ?[\d ?]{5,7}"+str(end)+"$"
    matches = re.finditer(pattern, text, re.M)
    for match in matches:
        print(match)

find_phones_with_area_code(604,78,text)

        

 



