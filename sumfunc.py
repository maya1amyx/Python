sum=0
list=[]

while sum==0 :
    answer=input("Add a number to your list and write sum when you are done ")
    if answer=="sum":
        for i in list:
            sum= sum+i
        print(sum)
    else:
        answer=int(answer)
        list.append(answer)
