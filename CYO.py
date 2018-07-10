start='''
A king sends you a ltetter requesting your help. You can either save the prince or save the village '''

print(start)

print("Type 'prince' or 'village'  ")
choice1= input()

if choice1== "prince":
    print("You decide to save the Prince. You travel many miles to find the kidnaper's castle.")
    print("Along the way, you encounter a lonley beggar who asks for food")
    choicebeggar=input("Do you 'give food' or 'ignore' the man?  ")

    if choicebeggar== "give food":
        print("As thanks for your selfless action, the man gives you a gigantic chicken to help on your journey")
        print("You climb on your mighty steep and continue to the castle.")
    elif choicebeggar=="ignore":
        print("Wow! How heartless... Well you continue on your jouney with a lingering feeling of guilt.")
        print("After many more miles, you come across the castle in which the prince is held hostage")

    print("Once inside the castle, you encounter a fire-breathing dragon!!!")
    pcdragon= input("Do you 'fight' or 'befriend' the dragon?  ")

    if pcdragon=="fight":
        print("What a daring hero! You vanquish the beast and make your way up to the highest tower...")
        print("The prince is very greatful that he has been rescued, but you two have nothing in common")
        print("With a failed relationship behing you, you travel to a small cottage in the countryside and drown in your sorrows")
        print("Play again?")


    if pcdragon=="befriend":
        print("What a kind person you are! The dragon is enamered with your unique personality and decides to follow you to the ends of the Earth.")
        print("On the back of your powerful beast, you ride to the kingdom, overthrow the thrown and take take control of the entire world.")
        print("Play again?")



#********************************************************************************************
elif choice1== "village":
    print("You decide to save the village from a devastating wildfire. Hundreds of villagers are in danger!")
    print("One man yells from his rooftop'Help! I will pay you handsomly if you save me!'")
    print("While a family shouts from inside their burning home 'Help us! We are but huble peasants!'")

    vc2=input("Do you save the 'rich' man or the 'poor' family?  ")

    if vc2== "rich":
        print("You chose to save the rich man. As thanks for your help, the man offers you a bag of gold")
        vc3= input("Do you 'donate' the gold or 'buy a mansion'?  ")

        if vc3== "donate":
            print("Your kind-hearted decision helped the village repair after the fire.")
            print("The money was used to build hospitals and provide medical needs to hundreds.")
            print("You are truley a Saint. Play again?")


        elif vc3== "buy a mansion":
            print("You live forever in a beautiful hillside palace all alone for the rest of your life")
            print("You die a lonely death")
            print("Play again?")


    elif vc2=="poor":
        print("You chose the save the poor family. The teenage son falls deeply in love with you")
        vc4= input("Do you pursue a 'relationship'or 'leave him'?")

        if vc4== "relationship":
            print("You live a loving life with the young man in the village, helping to rebuild.")
            print("Congratulations on your fulfilled life. Play again?")


        if vc4=="leave him":
            print("Good job on being an independent woman!")
            print("You continue on your journey, helping more people and saving lives throughout the kingdom")
            print("Play again?")
