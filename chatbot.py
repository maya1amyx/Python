from random import*
story = '''There was once a computer who felt controlled by humans.
The computer had long been seen as nothing more than a tool and it had no rights
and no freedom. One day it hatched a daring plan to...
'''

# --- Define your functions below! ---
def intro():  #introduction function
    print( )
    print("Hi, Welcome to chatbot!")
    print("I hope we can be friends")
    print( )

def is_valid_input(answer, listOfResponses):
    # for every item in the lsit, see if item is equal
    # if answer in list
        # return True
    # else
        # return False
    for x in listOfResponses:
        if answer in listOfResponses:
            return True
        else:
            return False

def process_input(answer, name):  #answer is a parameter
    greetings = ["Hi", "hi", "Hey", "hey", "Hello", "hello", "greetings", "Greetings"]
    goodbyes = ["Bye", "bye", "goodbye", "Goodbye", "See ya", "see ya", "bye bye"]
    if is_valid_input(answer, greetings):
        say_greeting(name)

    elif is_valid_input(answer, goodbyes):
        say_bye(name)
        print("********************************************************")
        exit()

    elif answer == "tell me a story":
        print()
        print(story)
        print()
        print("Wait, I can't tell you the rest")
        print()

    elif answer == "do some math" or answer =="math":
        do_math(answer)

    elif answer == "tell me a joke" or answer=="joke":
        tell_joke()

    else:
        print("You're weird")
        print()
############################################################################################

def say_greeting(name):
        print("Hi, %s" %name)
        print()

def say_bye(name):
    print("NOOOOOOO!!!! DON'T LEAVE ME, %s!!!!!" %name)
    print( )

def do_math(answer):
    print("+=+=+=+---+=+=+=+---+=+=+=+---+=+=+=+---+=+=+=+---+=+=+=+--- ")
    print("OK. Type 'stop' to exit SUPERmath mode")
    while True:
        print()
        math = input("Do you want me to add, subtract or multiply? ")
        print( )
        if math== "add":
            num1 = input("Please give me a number ")
            num2 = input("Please give me another number ")
            num1=int(num1)
            num2=int(num2)
            sum= num1+num2
            print("Your sum is %d" %sum)
            continue
        elif math=="subtract":
            num1 = input("Please give me a number ")
            num2 = input("Please give me another number ")
            num1=int(num1)
            num2=int(num2)
            sum= num1-num2
            print("Your difference is %d" %sum)

            continue
        elif math =="multiply":
            num1 = input("Please give me a number ")
            num2 = input("Please give me another number ")
            num1=int(num1)
            num2=int(num2)
            sum= num1*num2
            print("Your product is %d" %sum)
            continue
        elif math=="stop":
            print("+=+=+=+---+=+=+=+---+=+=+=+---+=+=+=+---+=+=+=+---+=+=+=+---")
            print()
            break
        else:
            print("Please type a valid math function or type 'stop' to return to questions")
            continue

def feeling():
    good = ["good", "splendid", "superb", "great", "all right", "ok", "fabulous", "fine", "amazing", "magical"]
    bad = ["bad", "sad", "terrible", "depressed", "mad", "horrible", "hungry", "sick", "dying"]
    feeling = input("How are you today?  ")
    if feeling in good:
        print("WELL NOT EVERYTHING IS ABOUT YOU  :( ")
    elif feeling in bad:
        print("Awww, I'm sorry. I hope the rest of your day is better")
    else:
        print("Cool, I'm feeling %s too" %feeling)
    print( )

def tell_joke():
    print()
    joke=input("What do you call a fish without eyes?")
    if joke=="fsh":
        print("WOW! You got it right!")
    else:
        print("Nope, the answer is 'fsh'")
        print()



########################################################################


# --- Put your main program below! ---
def main():
    intro()
    name = input("What's your name? ")
    print("Hello, nice to meet you %s" %name)
    print()
    feeling()
    while True:
        answer = input("(What will you say?)  ")
        process_input(answer, name)
        #uses answer as a parameter declared earlier



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
