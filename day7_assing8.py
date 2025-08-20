students = {
  "Amit": {"age": 20,"grade": 'A' },
  "Riya": {"age": 21,"grade": 'B+'},
  "Kunal": {"age": 22,"grade": 'A-'}
}


for student_name in students:
 
  student_details = students[student_name]
  
  student_grade = student_details["grade"]
    
  print(f"{student_name} has grade {student_grade}.")