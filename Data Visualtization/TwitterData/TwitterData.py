import json

tweets = open("tweets.json", "r")
tweetData = json.load(tweets)
tweets.close()

# Print the first tweet from the list, with index 0
print("The first tweet is", tweetData[0], "\n") #\n breaks a line
print("The text from the first tweet is:  ", tweetData[0]["text"])

#loop through each dictionary and print out the text from each tweets
for tweets in range(len(tweetData)):
    print("Tweet text:  ", tweetData[tweets]["text"], "\n")

#loop through each dictionary and print out the id number from each tweets
for tweets in range(len(tweetData)):
    print("Tweet id:  ", tweetData[tweets]["id"], "\n")

# for tweets in tweetData:
#     print("Tweet timestamp:  ", tweetData["created_at"], "\n")

print("There are ", len(tweetData), "tweets in the list \n")
