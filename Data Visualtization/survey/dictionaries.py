# dictionaries are used to save keys and their values
# each "word" we look up is the key
# and the "definition" would be the value

favorite_colors = {
    'person1' : 'black', # person1 is the key, black is the value
    'person2' : 'red',
    'person3' : 'blue',
    'person4'  : 'green',
    'person5' : 'yellow'
}

print("Person4's favorite color is ", favorite_colors["person4"], "\n")

acronyms = {
    "BLT" : "Bacon Lettuce Tomato",
    "API" : "Application Programming Interface",
    "LED" : "Light Emitting Diode"
}

student = {
    "name" : "firstName lastName", # name is the key, firstName lastName
    "age"  : 17,
    "courses" : ["math", "cs"]
}

print("The student dictionary: ")
print(student, "\n") # outputs entire student dictionary

print("The student name: ")
print(student["name"], "\n") # outputs only student's name

# Tip: Use .get() so you dont get KeyError and you can modify the error msg
print("The student name: ")
print(student.get("name"), "\n") # outputs only student's name
print("The student phone: ")
print(student.get("phone"), "\n") # displays "None"
print("The student name with my new error msg: ")
print(student.get("phone", "Phone Not Found"),"\n") # displays "Phone Not Found"

# -------------------------------------------------

# To UPDATE/CHANGE the dictionary use .update()
student.update({
    "name" : "firstNameUpdated lastNameUpdated",
    "age"  : 18,
    "courses" : ["biology", "physics"]
})

# run the same print statements for updated dictionary


print("The student dictionary after update: ")
print(student, "\n") # outputs entire student dictionary

print("The student name: ")
print(student["name"], "\n") # outputs only student's name

# Tip: Use .get() so you dont get KeyError and you can modify the error msg
print("The student name: ")
print(student.get("name"), "\n") # outputs only student's name
print("The student phone: ")
print(student.get("phone"), "\n") # displays "None"
print("The student name with my new error msg: ")
print(student.get("phone", "Phone Not Found"),"\n") # displays "Phone Not Found"

# To DELETE a key from the dictionary use del
del student["age"]

# dictionary result after deletion
print("The student dictionary after age has been deleted: ")
print(student, "\n") # output entire dictionary, won't see age since it's deleted

# To ADD a key and value
student["age"] = 18
print("The student dictionary after age has been added back: ")
print(student, "\n") # make sure it's been added

# To DELETE you can also use .pop()
# you can also save it in a variable
age = student.pop("age")
print("The student dictionary after age has been popped: ")
print(student, "\n")
print("The age we popped: ")
print(age, "\n") # prints age that we popped

# add it back
student["age"] = 18

# ---------------------
    # To loop through a dictionary

# to see the length of the dictionary:
# should be 3 for name, age and courses
print("The length of the dictionary is ")
print(len(student), "\n")

# to see the keys:
print("The keys in this dictionary are ")
print(student.keys(), "\n")

# to see the values:
print("The values in this dictionary are ")
print(student.values(), "\n")

# to see the keys AND values:
print("The keys AND values in this dictionary are ")
print(student.items(), "\n")   # displays key and value pairs

# Using a FOR loop
print("Using a for loop: ")
for key, value in student.items():
    print(key, value)

# ---------------------------
    # Full Terminal Output

'''
    Person4's favorite color is  green

    The student dictionary:
    {'name': 'firstName lastName', 'age': 17, 'courses': ['math', 'cs']}

    The student name:
    firstName lastName

    The student name:
    firstName lastName

    The student phone:
    None

    The student name with my new error msg:
    Phone Not Found

    The student dictionary after update:
    {'name': 'firstNameUpdated lastNameUpdated', 'age': 18, 'courses': ['biology', 'physics']}

    The student name:
    firstNameUpdated lastNameUpdated

    The student name:
    firstNameUpdated lastNameUpdated

    The student phone:
    None

    The student name with my new error msg:
    Phone Not Found

    The student dictionary after age has been deleted:
    {'name': 'firstNameUpdated lastNameUpdated', 'courses': ['biology', 'physics']}

    The student dictionary after age has been added back:
    {'name': 'firstNameUpdated lastNameUpdated', 'courses': ['biology', 'physics'], 'age': 18}

    The student dictionary after age has been popped:
    {'name': 'firstNameUpdated lastNameUpdated', 'courses': ['biology', 'physics']}

    The age we popped:
    18

     The length of the dictionary is
    3

     The keys in this dictionary are
    dict_keys(['name', 'courses', 'age'])

     The values in this dictionary are
    dict_values(['firstNameUpdated lastNameUpdated', ['biology', 'physics'], 18])

     The keys AND values in this dictionary are
    dict_items([('name', 'firstNameUpdated lastNameUpdated'), ('courses', ['biology', 'physics']), ('age', 18)])

    Using a for loop:
    name firstNameUpdated lastNameUpdated
    courses ['biology', 'physics']
    age 18
'''
