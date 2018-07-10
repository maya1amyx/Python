#Functions
#   remove(element)--removes element from the list
#   append(element)--adds an element to the end of the list
#   insert(index, element)--inserts an element in a SPECIFIC index
#   sort()--sorts the list in ascending order alphabetically or numerically
#   reverse() --reverse the list

list = [16, 7, 81, 40, "food"]
print(list)

list.remove(list[2])  #removes index 2 from list
list.append(500)

print(list)

list.insert(3, "lunchtime")
print(list)

list.remove("food")
list.remove("lunchtime")

list.sort()
print(list)
