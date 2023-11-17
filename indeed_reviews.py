def company_reviews(name):
    from selenium import webdriver 
    from selenium.webdriver.chrome.service import Service as ChromeService 
    from webdriver_manager.chrome import ChromeDriverManager 
    from selenium.webdriver.common.by import By
    from bs4 import BeautifulSoup
    from time import sleep
    
    options = webdriver.ChromeOptions() 
    
    # run browser in headless mode 
    #options.headless= True 
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    options.add_argument('user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')
    # instantiate driver 
    driver = webdriver.Chrome(service=ChromeService( 
        ChromeDriverManager().install()), options=options) 
    url = 'https://in.indeed.com/companies?from=gnav-homepage' 
    
    
    driver.get(url) 
    sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div/div[1]/form/div/div[1]/div/div/div/span/input").send_keys(name)
    driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div/div[1]/form/div/div[2]/button").click()
    sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div/div[2]/section/div[1]/div[1]/div/div[2]/div[1]/a").click()
    
    details=BeautifulSoup(driver.page_source,"html5lib")
    driver.close()
    indeed_reviews=details.find_all("span",{"class":"css-1n9w1js e1wnkr790"})
    rating_this_year_with_tag=details.find_all("g",{"class":"css-n3w4ap eu4oa1w0"})
    print(rating_this_year_with_tag)
    for i in rating_this_year_with_tag:
            x=str(i)
            finding_class=x.find("eu4oa1w0")
            finding_out=x.find("out")
            p=x[finding_class+60:len(x)-finding_out]
            try:
                rating=float(p[:-56])
            except:
                 rating=float(p[:-57])

    indeed_reviews_without_tag=[]
    for i in indeed_reviews:
        x=str(i)
        finding=x.find("e1wnkr790")
   
        indeed_reviews_without_tag.append(x[finding+11:-7])

    #print(indeed_reviews)
    return rating,indeed_reviews_without_tag

#company_reviews("tata communications")
