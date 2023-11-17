import requests 
from instagram import scrape_data
import re
from bs4 import BeautifulSoup 

def social_media_scrap(url):
    r = requests.get(url) 
    
    # Parsing the HTML 
    soup = BeautifulSoup(r.content, 'html.parser') 
    x=[]
    # find all the anchor tags with "href"  
    for link in soup.find_all('a'): 
        x.append(link.get('href'))
        #print(link.get('href'))
    #print(x)
    urls=[]
    for i in x:
        if i!=None:
            if "facebook" in i:
                urls.append(i)
            elif "instagram" in i:
                urls.append(i)
            elif "linkedin" in i: 
                urls.append(i)
            elif "youtube" in i:
                urls.append(i)
            elif "twitter" in i:
                urls.append(i)
    #print(urls)
    socia_media={"instagram":None,"facebook":None,"twitter":None,"youtube":None,"linkedin":None}
    for i in urls:
        if "instagram.com" in i:
            socia_media["instagram"]=i 
        elif "facebook.com" in i:
            socia_media["facebook"]=i 
        elif "twitter.com" in i:
            socia_media["twitter"]=i 
        elif "youtube.com" in i:
            socia_media["youtube"]=i
        elif "linkedin" in i:
            socia_media["linkedin"]=i 
        
    #print(socia_media["instagram"])
    return socia_media
def followers_count(s):##counting followers
    count=scrape_data(s)
    return count
    


 