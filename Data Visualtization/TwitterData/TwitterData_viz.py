import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#  Get the JSON data
tweetFile = open("Tweets_Big.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

print("***********************************************************")
#####print("The text from the first tweet:  ", tweetData[0]["text"])

#Create sentiment lists
polaritylist = []

# Get sentiment data including for loop and Text Blob
for tweet in tweetData:
    #Declare a vairable and declare the TextBlob library
    textBlob = TextBlob(tweet["text"])

    #tests the tweets for positive, negative language
    #Positive words are +1 and negative are -1 and neutral are 0
    polaritylist.append(textBlob.polarity)

#print out polarity list
####print(polaritylist, "\n")



#Create Histogram with polarity and BioInsights
plt.hist(polaritylist, bins = [-1.0, -.75, -.50, -.25, 0, .25 , .50, .75, 1.0])

# set the x and y lables
plt.xlabel("Polarities")
plt.ylabel("Number of Tweets")

# give the histogram a title
plt.title("Histogram of Tweet Polarity")

#set axis to fit data range, make a grid appear and show the data
#plt.axis([-1.0, 1.0, 0, 2300])
plt.grid(True)
plt.show()

#print("There are ", len(tweetData), "tweets in the list \n")
