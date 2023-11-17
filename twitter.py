"""
This Python code is designed to scrape the number of followers from a Twitter profile. 
The code uses Selenium for web automation, BeautifulSoup for HTML parsing, and 
the ChromeDriverManager to manage the ChromeDriver.


"""

def twitter_scrape(url):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from time import sleep
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service as ChromeService 
    from bs4 import BeautifulSoup  
    from selenium.webdriver.common.action_chains import ActionChains

    username = "hrithikpaul2001@gmail.com"
    password = "hrithik@123"
    phone="6296821825"
    #options=Options()
    options = webdriver.ChromeOptions() 

    # run browser in headless mode 
    options.headless= True 

    # instantiate driver 
    driver = webdriver.Chrome(service=ChromeService( 
        ChromeDriverManager().install()), options=options) 
    actions = ActionChains(driver)

    driver.get("https://twitter.com/login")
    sleep(4)
    try:
        driver.get("https://twitter.com/login")
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(username)
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(phone)
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div').click()
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(password)
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
        sleep(2)
    except:
        driver.get("https://twitter.com/login")
        sleep(4)
        driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(username)
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
        sleep(2)
    # driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(phone)
        #sleep(4)
        #driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div').click()
        #sleep(4)
        driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(password)
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
        sleep(2)
        
    driver.get(url)
    sleep(2)
    ps=BeautifulSoup(driver.page_source,"html5lib")
    followers_of_twitter_tag=ps.find_all("span",{"class":"css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"})
    #print(followers_of_twitter_tag)
    driver.close()
    for j in range(len(followers_of_twitter_tag)):
        x=str(followers_of_twitter_tag[j])
        find_unset=x.find("unset")
        main_text=x[find_unset+8:-7]
        #main_part.append(main_text)
        if "Followers" in x:
        # print(x)
            break 
    followers_twitter=str(followers_of_twitter_tag[j-1]) 
    followers_twitter=followers_twitter[94:-7]
    if "K" in followers_twitter:
        followers_twitter=float(followers_twitter[:-1])*1000
        #print(finding[finding_index+8:-7])
        
    print(followers_twitter)
    return followers_twitter


    #main_part.append(x[find_unset+8:-7])
#posts_details_with_tag=ps.find_all("span",{"class":"css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"})

#print(posts_details_with_tag)