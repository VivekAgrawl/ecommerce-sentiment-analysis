import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
import numpy as np
import preprocessing as t1
import nltk_preprocessing

def sentiment():
    df = t1.rename_columns()
    sentiments = SentimentIntensityAnalyzer()
    # Create sentiment column
    sentiments_list = []
    # Calculate sentiment scores for each review and assign 'positive' or 'negative' based on the scores
    # Iterate through each review text in the 'reviews_text' column
    for review_text in df['reviews_text']:
        # Calculate the sentiment scores using polarity_scores() method
        sentiment_scores = sentiments.polarity_scores(review_text)
        
        # Extract the positive and negative sentiment scores
        positive_score = sentiment_scores['pos']
        negative_score = sentiment_scores['neg']
        
        # Compare positive and negative sentiment scores
        # Assign sentiment label based on which score is greater
        if positive_score > negative_score:
            sentiment_label = 'positive'
        else:
            sentiment_label = 'negative'

        # Append the sentiment label to the 'sentiments' list
        sentiments_list.append(sentiment_label)
    
    # Add the 'sentiment' column to the DataFrame
    df['sentiment'] = sentiments_list
    return df

def process_text():
    df = sentiment()
    # Tokenize the reviews_text column using nltk's word_tokenize function
    df['reviews_text'] = df['reviews_text'].apply(word_tokenize)
    # Normalize the tokenized words using the normalize function from settings
    df['reviews_text'] = df['reviews_text'].apply(nltk_preprocessing.normalize)
    return df

def export_the_dataset():
    # Call process_text() to get the cleaned dataset with sentiment analysis and tokenization
    df = process_text()
    # Export the cleaned dataset to a new CSV file named 'ecommerce.csv'. use index = False.
    df.to_csv('ecommerce.csv', index = False)
    return df



# TASK 4: Load the Cleaned dataset 'ecommerce.csv' to the database provided.
# follow the instruction in the Task 5 description and complete the task as per it.

# check if mysql table is created using "ecommerce"
# Use this final dataset and upload it on the provided database for performing analysis in MySQL
# To run this task click on the terminal and click on the run project



