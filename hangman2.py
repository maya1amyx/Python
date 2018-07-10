# 1. Enter a word. Stores word as a variable
# 2. Repeat until win or loose condition is met
    # Print dashes to represent number of letters. Print lives left. Print letters guessed already
    # Guess a letter.
    # If the letter is in word, replace it in the dashes
    # If the letter is not in word, take away one life
# if win condition met, Print "you win" and exit()
# if lose condition met, Print "you lose" and exit()

while True:
    word = input("Type a word for someone to guess. The word can not have any repeating letters:")
    word = word.lower()# Converts the word to lowercase
    if(word.isalpha() == False):
        print("That's not a word")
    else:
        break


letters_used=[]
index=0
lives=7
loose=False
win=False
dashes=[]
location=0
count=0

space= '''














'''

for x in word:
    dashes.append("-")

print(space)

while loose==False or win==False:
    print("======================================")
    print("You have %d lives" %lives)
    print("Letters used:")
    print(letters_used)
    print(" ")
    print(dashes)
    print("Guess a letter")
    letter = input()

    if len(letter)>1 or (letter.isalpha() == False):
        print("You must enter a single, alphabetical letter")
        continue
    if letter in letters_used:
        print("You've already guessed this letter")
        continue
    if letter in word:
        print("Yay! You got a letter!")
        count += 1
        letters_used += letter
        location = word.index(letter)

        dashes.pop(location)   # GOTTA FIGURE THIS OUT!!!!
        dashes.insert(location, letter)
        #dashes.remove(word.index(letter))
        #dashes.insert(word.index(letter), letter)
        if count == len(word):
            print("***************************************")
            print(" ")
            print("You win!")
            print("The word was %s" %word)
            print(" ")
            exit()

    else:
        print("That letter is not in the word")
        lives-=1
        letters_used += letter
    if lives==0:
        print("You are out of lives!")
        print("The correct word was %s" %word)
        loose=True
        break
