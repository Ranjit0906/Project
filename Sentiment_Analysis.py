# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 11:34:40 2022

@author: Rohit Rankhamb
"""

# Import required Libraries
import pickle
import streamlit as st
import re
from textblob import TextBlob

from PIL import Image
image = Image.open("D:\P123 Project\Sentiment_Analysis_Image.jpg")
st.image(image)

    
# Import Model 
model = pickle.load(open("D:/P123 Project/final_model.pkl",'rb'))


# Creating a function for Data cleaning
def clean(text):
    # Removes all special characters and numericals leaving the alphabets
    text = re.sub('[^A-Za-z0-9_]+', ' ', str(text))
    text = re.sub('#',' ',str(text))
    text = re.sub('https?:/\/\[A-Za-z0-9\.\/]+',' ',str(text))
    text = str(text).lower()
    text = re.remove_stopwords(text)
    return text


# Creating a function for Analysis

def get_sentiment(text):
    blob = TextBlob(text)
    sentiment_polarity = blob.sentiment.polarity
    sentiment_subjectivity = blob.sentiment.subjectivity
    
    if sentiment_polarity<0:
        sentiment_label = "This review is Negative"
    elif sentiment_polarity>0:
        sentiment_label = "This review is Positive"
    else:
        sentiment_label = "This review is Neutral"
        
    result = {'polarity':sentiment_polarity,
              'subjectivity':sentiment_subjectivity,
              'sentiment':sentiment_label}
    return result
    

def main():
    # Title
    st.title('Review Sentiment Analysis')
    st.markdown('This application is all about review sentiment analysis of iPhone 4s. We can analyse review of the customer using this streamlit app.')
    reviewText = st.text_input('Enter your product review ', '')   
    
    diagnosis = ''
    
    # Creating a button for analysis
    if st.button('Analyse'):
        diagnosis = get_sentiment(reviewText)
        
    st.success(diagnosis)
    
if __name__=='__main__':
        main()


        
