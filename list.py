WIT = ["Cindy", "Dorthey", "Aprille", "Amanda" , "Jesse"]
# index:  0        1           2          3         4
#heights = [5.9, 6.1, 4.8, 5.4, 5.3, 5.6]

print (WIT) #Print elements in the list
print("The number of elements in my list:  ")
print(len(WIT)) #Prints the length of the list

print("Cindy" in WIT) #Lets you know if something is in the list. Returns True
print(6 in WIT) # Returns false

print("Print element 3 in my list")
print(WIT[3])  #returns Amanda

print("Print element 3, character 2 in my list:  ")
print(WIT[3][2])  #returns a

print("Print element 3 and 4 in my list")
print(WIT[3] + WIT[4])

print("All of the items on my list:  ")
for num in WIT:   # num is a place holder. It signifies each element in the list
    print(num)    # num can be replaced with anything alse, like i
    #prints out each element in the list...

#does the same thing as:...
# for i in range(len(WIT)):
#     print(WIT[i])

#What if it's a super long list, and you want to know the last element, but you don't know its index
last_element = len(WIT)-1  #Returns index 4

print("What is the last item on my list?  ")
print(WIT[last_element])
# you can hashtag out multiple lines with      command + /
