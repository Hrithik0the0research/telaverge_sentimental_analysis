"""
This Python code appears to perform sentiment analysis on reviews related to a company.

"""
import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from company import company_name
from indeed_reviews import company_reviews
from youtube import youtube_comments
nltk.download("vader_lexicon")##download vader_lexicon
analyzer=SentimentIntensityAnalyzer()
def sentiment_analyse(name):##define sentiment_analyse
    indeed_reviews=""
    rating=0   
    rating,indeed_reviews=company_reviews(name)
    
 
    name=company_name(name)
    reviews,social_media_links=youtube_comments(name)
    print(social_media_links["instagram"])
    find_com=social_media_links["instagram"].find(".com")
    find_id=social_media_links["instagram"][find_com+5:len(social_media_links["instagram"])-1]
    if indeed_reviews!="":
        reviews=reviews+indeed_reviews
        
    base=[]
    pos_neg=[]
    for i in reviews:
        scores=analyzer.polarity_scores(i)
        pos_neg.append(scores)
    pos,neg=0,0

    for i in pos_neg:
        if i['pos']>=0.5:
            pos+=1
        elif i['neg']>=0.5:
            neg+=1 
     
    return reviews,find_id,pos,neg,social_media_links,rating
"""
The purpose of this code seems to be analyzing sentiment in reviews related to a company, 
extracting relevant social media links, and providing counts of positive and negative reviews. 
The sentiment analysis is done using the VADER (Valence Aware Dictionary and sEntiment Reasoner) 
sentiment analysis tool from NLTK.

"""

