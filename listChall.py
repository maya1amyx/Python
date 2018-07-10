# RANDOM NAME GENERATOR

# from random import*
#
# aList= ["Epic", "Top", "Serial Killer", "Apple", "Box", "Mind", "Space", "Monkey", "Jungle","True", "False", "Time", "Clock", "Light", "Dark", "walls", "Icon", "Supercalifragalisticexpialidocious"]
#
# aRandomIndex = randint (0, len(aList)-1)
# aRandomIndex2 = randint (0, len(aList)-1)
#
# if aRandomIndex==aRandomIndex2:
#     aRandomIndex = randint (0, len(aList)-1)
#     aRandomIndex2 = randint (0, len(aList)-1)
#
# elif aRandomIndex != aRandomIndex2:
#     print("Here's your random name:  ")
#     print(aList[aRandomIndex] + "-" + aList[aRandomIndex2])

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# FINDING AN AVERAGE OF A LIST

# 1. Create the list
# 2. Add all the values together
# 3. Divide by the length
# 4. Print the average

ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]

sum= sum(ages)
average= sum/len(ages)

print( " ")
print("This is the average of some numbers: %d" %average)

# OR


ages2 = [7,98,74,3,12,35,65,14,98,45,65,24]

sum2=0

for x in ages2:
    sum2 += x

print("This is the sum of some numbers: %d" %sum)
print(" ")
