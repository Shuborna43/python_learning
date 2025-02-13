
# #string literal (``)

# #name_1 = '''Wadi is a \'good\' boy'''

# name_2 =  """Wadi is 7'5" tall"""

# name_3 =  'Wadi is 7\'5" tall' 

# print ("Wadi is 7'5", end = "")

# print ('" tall')

# #print (name_2, name_3)

# name_4 = "Wadi"

# name_5 = "Saad"

# print (name_4 + " " + name_5)

# name_6 = "Adyan "

# number = 5

# mult = number * name_6

# print ( mult )

# name_7 = "Wadi" #%s

# quantity = 8907 #%d

# price = 8.9678 #%f

# text = "%s purchased %d socks for $%.3f for each" % (name_7, quantity, price)  #string formatting

# print (text)

# minimal field width 
#%7s

# name_8 = "Adyan"
# age = 13 

# print ("Name: '%7s'" %name_8) #right justification
# print ("Name: '%-7s'" %name_8) #left justification 

#zero padding 
#%03d

# number = 45

# print ("Number: '%07d'" %number) #0 padding

# number = 0xabc123

# print ("the number is %X" %number)

# number = 0xABC123

# print ("the number is %x" %number)

#using f-string 

# name_7 = "Wadi" #%s
# quantity = 8907 #%d
# price = 8.9678 #%f

# text = f"{name_7} purchased {quantity} socks for {price} each" #dynamically variable accessing 

# print (text)

first_name = "Wadi"
last_name= "Ahmad"
current_year = 2025

text_1 = f"{first_name} {last_name} is in class VII in {current_year}"
text_2 = f"{first_name} {last_name} is in class VII in %d" % (current_year)

#"%s purchased %d socks for $%.3f for each" % (name_7, quantity, price)

print (text_1)
print (text_2)




