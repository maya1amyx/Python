anExample = "Ada!"

print("Each character in my string:  ")
for letter in anExample:
    print(letter)  #Prints each character individually

print("The number of characters in my string 'Ada!' :  ")
print(len(anExample))  #Gives us the length of the string. Answer gives back 4, the number of characters.

print("Are the letters 'da' in my string?  ")
print("da" in anExample)   #Returns TRUE

print("Are the letters 'zerrgrgrur' in my string?")
print("zerrgrgrur" in anExample) #Returns FALSE

print("Prints a specific letter in my string:  ")
print(anExample[2])  #Returns a

print("Prints two letters together: ")
print(anExample[1] + anExample[3])  #Concatination  # Returns d!
