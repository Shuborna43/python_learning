student_name = ["AA","BB","CC","DD","EE"]
student_ID = [111,222,333,444,555]
student_section = ["sec-A","sec-B","sec-C","sec-D","sec-E"]
student_CGPA = [3.5,3.4,4.0,3.1,3.8]
student_address = ["DHK","KHUL","RAJ","DHK","RAJ"]
student_class = ["V","III","V","I","X"]


student_data = {}

for i in range (0,len(student_name)):
  student_data[student_name[i]] = [student_ID[i],student_section[i],student_CGPA[i],student_address[i],student_class[i]]
print(student_data)

for j in range (0,len(student_CGPA)):
  for p in range (0,len(student_CGPA)-1):
    if student_CGPA[p]<student_CGPA[p+1]:
      student_CGPA[p],student_CGPA[p+1]=student_CGPA[p+1],student_CGPA[p]
    else:
      continue
print (student_CGPA)

print(sorted(student_data.items()))
print(sorted(student_data.items(), key=lambda x: x[1][2], reverse=True))


