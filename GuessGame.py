from random import* #imports ability to generate random number

aRandomNumber = randint(1, 10)
Ans = 0

for Ans in range(3):
    Ans += 1
    guess = input("Guess a number between 1 and 10. You have 3 tries...  ")

    if not guess.isnumeric():  #checks if a string is only digits 0 to 9
            print("That's not a positive whole number, try again")
    else:
        guess = int(guess) #converts string to an integer
        if guess > aRandomNumber:
            print ("That's too high. Try again...")
            continue
        elif guess < aRandomNumber:
            print("That's too low. Try again...")
            continue
        elif guess==aRandomNumber:
            print("Yay! You got it! The answer is %d. Play again?" % aRandomNumber )
            break

if Ans==3 and guess!=aRandomNumber:
    print("Sorry, you are out of turns. The correct answer was %d." % aRandomNumber)
