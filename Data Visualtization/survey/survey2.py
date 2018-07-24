import json
questions = [  #brackets for lists
    "What is your name?",
    "What is your age?",
    "What grade are you in?"
]
keys = ["name", "age", "grade"]
all_users = []

done = "No"

while done =="No":

    answers = {} # curly brackets for dictionaries
    print("**************************************************")
    for items in range(len(questions)):

        user_answer = input(questions[items])
        answers[keys[items]] = user_answer  #updates the list with one of the keys and the user's input

    all_users.append(answers) #adds the new answers to the list of all answers
    print(all_users)


    finish = input("Are you done? (Yes or No):  ")
    if finish=="Yes":
        done="Yes"
    elif finish =="No":
        done = "No"


# Load data from JSON to Python
json_file_read = open("data.json", "r") # opens json file in reading mode "r"
json_old_data = json.load(json_file_read)#loads previous data

all_users.extend(json_old_data)  # adds to the old data
json_file_read.close()


# Write data from python to json
json_file_write = open("data.json", "w") # opens json in writing mode, "w"
json_file_write.write("[\n")

#loops through our list of all answers and adds them to the new list
for item in all_users:
    dump = json.dumps(item)
    json_file_write.write(dump)
    json_file_write.write(",\n")

json_file_write.write("\n]")
json_file_write.close()
