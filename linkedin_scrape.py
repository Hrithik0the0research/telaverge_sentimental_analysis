"""
This Python function, named linkedin_get(url), is designed to extract information from a LinkedIn profile, 
particularly the total number of followers and the total count of reactions from the user's posts. 
The function uses the Selenium web driver along with BeautifulSoup for web scraping.

"""
def linkedin_get(url): 
    from selenium import webdriver 
    from selenium.webdriver.chrome.service import Service as ChromeService 
    from webdriver_manager.chrome import ChromeDriverManager 
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from bs4 import BeautifulSoup  
    from selenium.webdriver.support.expected_conditions import visibility_of_element_located
    options = webdriver.ChromeOptions() 

    # run browser in headless mode 
    #options.headless= True 
    options.add_argument('--headless')
    options.add_argument('user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')
    # instantiate driver 
    driver = webdriver.Chrome(service=ChromeService( 
        ChromeDriverManager().install()), options=options) 
    login_url = 'https://www.linkedin.com/login?fromSignIn=true&trk=\guest_homepage-basic_nav-header-signin' 
    driver.get(login_url) 
    #time.sleep(5)
    USERNAME = "hrithikpaul2001@gmail.com"
    PASSWORD ="hrithik@123"
    elementID = driver.find_element(By.ID,'username')
    elementID.send_keys(USERNAME)
    elementID = driver.find_element(By.ID,'password')
    elementID.send_keys(PASSWORD)
    elementID.submit()


    profile_url = url
    
    driver.get(profile_url) 
    title = (
        WebDriverWait(driver=driver, timeout=10)
        .until(visibility_of_element_located((By.CSS_SELECTOR, "li")))
        .text
    )
    ps=BeautifulSoup(driver.page_source,"html5lib")##post scraping
    connections=ps.find_all("span",{"class":"link-without-visited-state"})
    social_reaction_counts_all_newly_post=ps.find_all("span",{"class":"social-details-social-counts__reactions-count"})
    #print(social_reaction_counts_all_newly_post)
    social_comments_counts_all_newly_posts=ps.find_all("button",{"class":"t-black--light social-details-social-counts__count-value t-12 hoverable-link-text"})
    #print(social_comments_counts_all_newly_posts)
    followers_count=ps.find_all("div",{"class":"org-top-card-summary-info-list__info-item"})
    driver.close()
    #print(followers_count)
    #name = ps.find_all('div',{"class":"ph5"})
    connections=str(connections)
    #finding_word_t_bold=connections.find("t-bold")
    #total_connections_number=connections[81:84]
    total_count_reactions=0
    for m in social_reaction_counts_all_newly_post:
        m=str(m)
        reactions_index=m.find("count")
        #print(int(m[reactions_index+25:reactions_index+28]))
        total_count_reactions+=int(m[reactions_index+25:-7])
    print("total_count_reactions",total_count_reactions)
    index_for_followers=str(followers_count[0]).find("item")
    #print(index_for_followers)
    followers_text=""
    for i in followers_count:
        if "followers" in str(i):
            #print(str(i[index_for_followers:]))
            followers_text=str(i)
    follwers=followers_text[index_for_followers+6:-18].strip()
    #print(follwers[:-10])
    total_followers=""
    for i in follwers[:-10]:
        
        if i!=",":
            total_followers+=str(i)
    print("total followes",int(total_followers))
    return total_followers,total_count_reactions

