
def main():

    print("***************************************************")
    print("Can your password survive a dictionary attack?")


    # Opens a file. You can now look at each line in the file individually with a statement like "for line in f:

    list = open("dictionary.txt","r")
    found=False

    # You will have to use .strip() to strip whitespace and newlines from the file and passwords
    test_password = input("Type in a trial password: ")
    test_password = test_password.lower()
    #test_password = test_password.strip()

    length=len(list.readlines())
    print(length)
    count=0
    print()

    #Write logic to see if the password is in the dictionary file below here:
    while count <= length:

        line = list.readline()

        if line.strip() == test_password.strip():
            print("You're password has been hacked")
            #found=True
            break
        elif line.strip() != test_password.strip():
            #print("1")
            count +=1
            continue

######################################################
if __name__=='__main__':
    main()
