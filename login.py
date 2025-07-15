def generate_password(first_name, last_name, student_id):
   

#   refirst_name = first_name.title()
#   relast_name = last_name.title()
#   n=len(student_id)
#   password_format = refirst_name[0:3]+relast_name[0:3]+student_id[n-3:n]
#   return password_format

  formatted_first = first_name.strip().capitalize() #strip=it removes leading and trailing spaces
  formatted_last = last_name.strip().capitalize()
  formatted_ID = student_id.strip() 


  if len(formatted_first) >= 3:
        first_part = formatted_first[0:3]
  else:
        first_part = formatted_first


  if len(formatted_last) >= 3:
        last_part = formatted_last[0:3]
  else:
        last_part = formatted_last


  if len(student_id) >= 3:
        id_part = formatted_ID[-3:]  # Get the last 3 characters
  else:
        id_part = formatted_ID

  password = first_part + last_part + id_part
  return password