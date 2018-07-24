import json
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt


#  Get the JSON data
# tweetFile = open("Tweets_Big.json", "r")
# tweetData = json.load(tweetFile)
# tweetFile.close()

print("***********************************************************")

d = path.dirname(__file__)

string = " "

# Read the whole text.
tweets = open("Tweets_Big.json", "r")
tweetData = json.load(tweets)
tweets.close()

for tweet in range(len(tweetData)):
    words = tweetData[tweet]["text"]
    string += words

print(string, "\n")

#text = path.join(d, string)

# Generate a word cloud image
wordcloud = WordCloud().generate(string)

# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(string)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()

#print("There are ", len(tweetData), "tweets in the list \n")
