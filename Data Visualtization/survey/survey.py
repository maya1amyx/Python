#lists

IsDone=False
all_users = []



def survey(all_users):
    print("******************************************************************")
    print("Welcome to the survey!")

    #defining local variables and lists and dictionaries
    questions = ["1. What is your favorite flavor of ice cream?  ", "2. What's your favorite animal?  ", "3. What's your favorite color?  "]
    keys = ["ice cream", "animal", "color"]
    survey = {}
    y=1

    #loops, asks each question and stores response
    while y <= len(questions):

        print( )
        answer= input( questions [y-1] )

        #checks if answer is alphabetical and at least a single character
        if len(answer)<1 or (answer.isalpha() == False):
            print("You must enter an apropriate answer")
            continue

        elif y< len(questions) and (answer.isalpha() == True):
            survey[ keys[y-1] ] = answer
            y+=1

        elif y==len(questions):
            #prints current keys and values
            print( )
            for key,value in survey.items():
                print(key, ":" , value)

            #Adds answers to all_users list
            all_users.append(survey)
            #Prints all_users responses
            print()
            print("Here's what everyone else has said: ")
            print(all_users)
            break

#third question and answer are not being saved to the dictionary.
#Also work on ability to edit

while IsDone==False:
    survey(all_users)
    print( )
    anotherResponse = input("Would you like to submit another response? Please type 'yes' or 'no' ")
    if anotherResponse=="yes" or anotherResponse=="Yes":
        continue
    elif anotherResponse=="no" or anotherResponse=="No":
        IsDone==True
        break
    else:
        print("That is not a valid response. Please type 'yes' or 'no'  ")
        break








#Asks if they want to edit or submit
# submitAns = input("Would you like to 'edit' your answers or 'submit'?  ")
#
# if submitAns == "edit" or submitAns =="Edit" :
#     print( )
#     edit = input("OK, which question do you want to edit? Please type the number:  ")
#
#     if len(edit) != 1 or (edit.isalpha() == True):
#         print("You must enter an apropriate number or 'submit' if you wish not to edit")
#         #continue
#     elif edit == "submit" or edit =="Submit":
#         print("Thanks for your response!")
#     else:
#         print(edit)
#
#
#
# elif submitAns == "submit" or submitAns=="Submit" :
#     print("Thanks for your response!")
# else:
#     print("Please type 'edit' or 'submit'  ")
#     continue
#

print("******************************************************************")
