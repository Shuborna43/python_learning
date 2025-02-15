# first_name = "Wadi"
# last_name = "Ahmad"
# years_employed = 10
# hourly_rate = 100.86

# #CSV data format

# CSV_1=f"{first_name}, {last_name}, {years_employed}, {hourly_rate}"
# CSV_2= first_name+","" "+last_name+","" " +str(years_employed)+","" " +str(hourly_rate)
# CSV_3= "%s, %s, %d, %.2f" % (first_name, last_name, years_employed,hourly_rate)  

# print (CSV_1)
# print (CSV_2)
# print (CSV_3)

#json data format (JavaScript object notation), array of objects

# numbers=[{
# 	    "first_name": "Susan",
# 		"last_name": "Lee",
# 		"experience": 18,
# 		“hourly_wage_cad": 34.58
# 	    }, 
#         {
# 	    "first_name": "Susan",
# 		"last_name": "Lee",
# 		"experience": 18,
# 		“hourly_wage_cad": 34.58
# 	    },
#         {
# 	    "first_name": "Susan",
# 		"last_name": "Lee",
# 		"experience": 18,
# 		“hourly_wage_cad": 34.58
# 	    }
#         ] 

#create a string in Json format: Array of objects [{},{},{}]


first_name = "Susan"
last_name = "Lee"
experience = 18
hourly_wage_cad = 34.58

# Json_format_1 = "{+'"'+first_name:"+'"'+ '"'+first_name+'"'+","+ '"'+"last_name:"+'"'+'"'+last_name+'"'+","+'"'+ "experience:"+'"'+ str(experience)+","+ '"'+"hourly_wage_cad:"+'"'+ str(hourly_wage_cad)+ "}"
# print (Json_format_1)

Json_format_2 = '{ "first_name": "%s", "last_name": "%s", "experience": "%d", "hourly_wage_cad": "%.2f"}' %(first_name, last_name, experience, hourly_wage_cad)  

print (Json_format_2)

# '''{"first_name": "%s", "last_name": "%s","years_Employed": "%d", "hourly_rate": "%.2f"}'''%(first_name, last_name, years_employed, hourly_rate)    
