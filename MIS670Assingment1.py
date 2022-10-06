#Import Library
import re
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import csv
import nltk
from nltk.corpus import stopwords
from nltk import FreqDist, word_tokenize
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


#Read in the file
review = []
openfile = open('MovieReviewData_HW2.csv', 'r')
positive_words = open('Bing_liu_positive.txt', "r").read().splitlines()
negative_words = open('Bing_liu_negative.txt', "r").read().splitlines()
# openfile = open('Challenge Lab #4 data/sampledata_wordfrequency.csv', 'r', encoding = "ISO-8859-1")
r = csv.reader(openfile)
for i in r:
# get the first column only (ignoring the second column)
    review.append(i)
openfile.close()

#Clean up
new_texts = []
flat_review = [''.join(ele) for ele in review]
documents = [re.sub("[^a-zA-Z]+", " ", document) for document in flat_review]
texts = [[word for word in document.lower().split()] for document in documents]
new_documents = [item for sublist in new_texts for item in sublist]
print(documents[:2])

# print(len(texts[:2]))
# for review in texts[:2]:
#     print(review)
#     print("\n")
#     for word in review:
#         #print(len(word))
#         if len(word) >= 3:
#             new_texts.append(word)
# print(len(new_texts))