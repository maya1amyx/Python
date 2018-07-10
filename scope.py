def say_hello():
    print("hi " + name)

name = "Maya"
#The variable is global. It is not declared inside of a function, so all functions can use it
# You do not need to use it as a parameter in the function say_hello, because it is global.
say_hello()

##################################################

def say_hello(name):
    print("hi " + name)

# now name cariable is a local variable bc it is declared inside a function
#So you have to use it as a parameter in the say_hello function

def main():
    name = ", Nice to meet you"
    say_hello(name)

#This runs the main code.. DONT TOUCH
if __name__=="__main__":
    main()

###################################################

def say_hello(name):
    print("hi " + name)

# now name cariable is a local variable bc it is declared inside a function
#So you have to use it as a parameter in the say_hello function

def main():
    user = "Maya"
    say_hello(user)  #We can even insert a different parameter

#This runs the main code.. DONT TOUCH
if __name__=="__main__":
    main()

######################################################

def sub(num1, num2):
    diff = num1 - num2
    return diff    #This signifies the end of the function and sends out the number to be picked up by another function.
    print diff  #Anything after return is ignored 

def main():
    print(sub(10, 2))

if __name__=="__main__":
    main()
