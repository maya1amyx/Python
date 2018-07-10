word = input("Type a word for someone to guess:")

# Converts the word to lowercase
word = word.lower()
# Some useful variables
guesses = []
lives = 7
length= len(word)


# Checks if only letters are present
if (word.isalpha() == False):
	print("That's not a word!")
    #word = input("Type a word for someone to guess:")
    #Asks again if the word is not made of letters
else:
    for lives in range(0): #
        for i in range(length):
            print("-")*len(word)
            guess = input("Guess a letter: ")
            if guess in word==True:
                print("The letter is in the word!")
                guesses.append()

            elif guess in word==False:
                print("That letter is not in the word")
