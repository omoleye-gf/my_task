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
# print(student["name"])
# print(student.get("age"))
# print(student.get("grade","Not Found"))
# # using pop()
# student.pop("course")
# # using popitem
# student.popitem()

# # 3. Using del keyword
# del student["course"]

# 4. Using clear() - removes all items
# student.clear()

# print(student)
person = {"name": "Emeka", "age": 30}

# # 1. keys()
# print(person.keys())

# # 2. values()
# print(person.values())
# # 3. items()
# print(person.items())
# 4. update()
person.update({"age": 31, "city": "Lagos"})
print(person)
students = {
    "student1": {"name": "Ada", "age": 20},
    "student2": {"name": "John", "age": 22}
}

print(students["student1"]["name"])  # Access nested data
# Define a dictionary
student = {"name": "Ada", "age": 20, "course": "Computer Science"}
# Loop through values
for value in student.values():
    print(value)
    # Loop through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
    # Storing a student's biodata
student = {
    "name": "Chinedu",
    "age": 19,
    "department": "Engineering",
    "subjects": ["Maths", "Physics", "Chemistry"],
    "is_full_time": True
}
print(f"Name: {student['name']}")
print(f"Subjects: {', '.join(student['subjects'])}")

# Storing a student's biodata
student = {
    "name": "Chinedu",
    "age": 19,
    "department": "Engineering",
    "subjects": ["Maths", "Physics", "Chemistry"],
    "is_full_time": True
print(f"Name: {student['name']}")
print(f"Subjects: {', '.join(student['subjects'])}")

# Create an empty dictionary
student = {}

# Add key-value pairs to it
student["name"] = "Goodness"
student["Interest"] = "AI"
student["Track"] = "AI_Dev"

print(student)


# List of dictionaries - Each student has their own dictionary
students = [
    {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
    {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
    {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
]

print(students[0]["Name"])   
print(students[1]["Track"])

# Create an empty dictionary
student = {}

# Add key-value pairs to it
student["name"] = "Goodness"
student["Interest"] = "AI"
student["Track"] = "AI_Dev"

print(student)
(edited)
# List of dictionaries - Each student has their own dictionary
students = [
    {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
    {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
    {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
]

print(students[0]["Name"])   
print(students[1]["Track"])  
(edited)


# Dictionary of dictionaries - Each student is keyed by their ID
students = {
  "AI010"   :  {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
  "AI020" :  {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
  "AI030"  :  {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
}

print(students["AI020"]
      ["Name"])   
print(students["AI030"]
      ["Track"])
  scores = {
    "python": [85, 78, 92],
    "pandas": [88, 74, 90],
    "Scikit-learn": [80, 95, 87]
}

print(scores["python"])    
print(score