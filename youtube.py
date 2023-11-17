"""

This Python code is designed to scrape YouTube comments from videos associated with a given YouTube channel. 
It uses Selenium for web automation, the ChromeDriverManager to manage the ChromeDriver, and 
the youtube_comment_downloader library to download YouTube comments. 



"""
##importing packages
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from youtube_comment_downloader import *
from itertools import islice
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService 
from srcaping import social_media_scrap
def youtube_comments(name):
    options = webdriver.ChromeOptions() #chromeoptions

    # run browser in headless mode 
    options.headless= True 

    # instantiate driver 
    driver = webdriver.Chrome(service=ChromeService( 
        ChromeDriverManager().install()), options=options) 

    social_media_links= social_media_scrap(name)#calling the social_media_scrap function from srcaping.py
    url=social_media_links['youtube']##getting youtube link

    driver.get(url)##getting status code and get the access token

    height = driver.execute_script("return document.documentElement.scrollHeight")##scroll to find out all posted video's comments
    previousHeight = -1

    while previousHeight < height:
        previousHeight = height
        driver.execute_script(f'window.scrollTo(0,{height + 10000})')
        time.sleep(1)
        height = driver.execute_script("return document.documentElement.scrollHeight")##js script to scroll

    vidElements = driver.find_elements(By.ID,'thumbnail')#finding id name with thumbnail from page source
    vid_urls = []##empty list
    for v in vidElements:
        vid_urls.append(v.get_attribute('href'))##getting attributes named href

    #print(vid_urls)
    downloader = YoutubeCommentDownloader()##calling the class and make object downloader
    x=[]
    for i in vid_urls:
        if i!=None:
            comments = downloader.get_comments_from_url(i, sort_by=SORT_BY_POPULAR)##get comments method has been called
            for comment in islice(comments, 10):
                x.append(comment['text'])

    return x,social_media_links##return the link and all reviews

