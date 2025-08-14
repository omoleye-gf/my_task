# The syntax of a dictionary
# dictionary_name = {keys1: value,key2: value2}
# creating dictionary
# student ={
#      "name":"Ada",
#      "age": 20,
#      "course": "Computer Science"
# }
# print(student)
# # using the dic() constructor
# student_info = dict(name="John", age=25, course="Maths")
# print(student_info)
# # empty dictionary
# empty_dict ={}
# print(empty_dict)
# # create a dictionary of numbers and their squares
# squares = {x: x**2 for x in range(1,6)}
# print(squares)
# # # with condition
# even_cube ={x:x**3 for x in range(1,10) if x % 2 ==0}
# # print(even_cube)
# # from Existing dictionary
# students = {"Ada": 85,"JOhn": 40,"Musa": 65}
# # Filter students who passed (score >= 50)
# passed_students={name: score for name,score in students.items()if score >=50}
# print(passed_students)
# # using string keys
# names =["Ada","John","Musa"]
# even_cube ={x:x**3 for x in range(1,30) if x % 4 ==0}
# # print(even_cube)
# # using string keys
# names =["Ada","John","Musa"]
# lengths ={name: len (name)for name in names}
# print(lengths)
# names =["Bola","Mat","Titi"]
# lengths ={name: len (name) for name in names}
# print(lengths)
# Define a dictionary
student = {"name": "Ada", "age": 20, "course": "Computer Science"}
# print(student)
# using get ()method
print(student["name"])
print(student.get("age"))
print(student.get("grade","Not Found"))
# Us