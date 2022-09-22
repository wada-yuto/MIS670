#import library
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords, wordnet
from nltk import FreqDist, word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from os import path
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

file_to_read = "reviews.txt"
positive_words = open("Bing_liu_positive.txt", "r").read().splitlines()
negative_words = open("Bing_liu_negative.txt", "r").read().splitlines()
text_file = open(file_to_read, "r").read().splitlines()

positive_review = []
neutral_review = []
negative_review = []

for review_text in text_file:
    review_clean = re.sub(r"[\(<>/)!#$%&'*+-.^_`|~:’“”?]",'',review_text)
    documents = [review_clean for document in review_text]
    token = [[word for word in document.lower()] for document in documents]
    for sentence in token:
        positive = 0
        negative = 0
        for word in sentence:
            if word in positive_words:
                positive += 1
            elif word in negative_words:
                negative += 1
        if positive-negative > 0:
            positive_review.append(sentence)
        elif positive-negative == 0:
            neutral_review.append(sentence)
        else:
            negative_review.append(sentence)
# the contents of each category showing in tokens
print("Hello world")
