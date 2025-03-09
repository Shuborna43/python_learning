# list comprehension: A shorter way to create a new list from another list based on conditions that we set
# countries = ["Bangladesh", "India", "Pakistan", "Bhutan", "Nepal", "Spain"]
# countries_with_e = [country for country in countries if "e" in country]
# print (countries_with_e)

# numbers = [3,6,8,2,0,4,55,88,28,9,44,54,234]
# even_number = [number for number in numbers if number % 2 == 0]
# print (even_number)

#list mutable operations: 
sports = ["football", "hokey", "cricket", "badminton", "volleyball", "handball" ]
slice_1 = sports[3:6]
print(slice_1) 

del sports[3]
print(sports)

sports.extend(["swimming", "shooting"])
print(sports)

sports.insert(3,"baseball")
print(sports)

remove_index = sports.pop(-2)
print(remove_index)

sports.sort()
print(sports)

sports.reverse()
print(sports)


