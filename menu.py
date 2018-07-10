from random import*

app = ["french fries", "breadsticks", "salad", "cheese balls", "fruit", "chips and salsa"]
entre = ["hamburger", "pasta", "quice", "pizza", "sushi"]
drinks = ["lemonade", "fountain drinks", "iced-tea", "coffee","beer", "wine"]
desserts = ["cake", "ice cream", "chocolate"]

indApp = randint (0, len(app)-1)
indEnt = randint (0, len(entre)-1)
inddri = randint (0, len(drinks)-1)
inddes = randint (0, len(desserts)-1)

print( )
print("Here's your random menu:  ")
print(app[indApp])
print(entre[indEnt])
print(drinks[inddri])
print(desserts[inddes])
print( )
#=============================================================================

syl = ("I like to rhyme words", "my code is the best", "Life is a mean thing", "Justine is awesome", "Shreya is so cool")
syl7 = ("Haikus make me really mad", "You will live a happy life", "The rain falls like beads through air", "I don't know what to do now")
syl5 = ("Refrigerator", "Somehow I will win", "I am so tired", "Sleep is calling me")

ran1 = randint (0, len(syl)-1)
ran2 = randint (0, len(syl7)-1)
ran3 = randint (0, len(syl5)-1)

print("Here's your random haiku:  ")
print(syl[ran1])
print(syl7[ran2])
print(syl5[ran3])
