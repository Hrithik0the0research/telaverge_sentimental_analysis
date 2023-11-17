import streamlit as st 
from sentiment import sentiment_analyse
from srcaping import followers_count
import pyrebase 
from linkedin_scrape import linkedin_get
from sending_mail import sending
from twitter import twitter_scrape

st.set_page_config(page_title='home', layout = 'wide', page_icon = 'logo.png', initial_sidebar_state = 'auto')
st.title("Welcome to sentiment_brand_analyze")
company_name=st.text_input("Enter the name of company")
firebaseConfig = {
  'apiKey': "AIzaSyApnxpPI5HRpsw9gh0HAj-pMivtLL-lqJs",
  'authDomain': "telaverge-34c91.firebaseapp.com",
  'databaseURL': "https://telaverge-34c91-default-rtdb.firebaseio.com",
  'projectId': "telaverge-34c91",
  'storageBucket': "telaverge-34c91.appspot.com",
  'messagingSenderId': "1008337255380",
  'appId': "1:1008337255380:web:96c5a0179d37143bdeb441",
  'measurementId': "G-LSN760BNCS"
}

if company_name!="" and company_name!=" ":
    firebase=pyrebase.initialize_app(firebaseConfig)
    db=firebase.database()
    database_keys={}
    for j in db.get():
        database_keys[j.key()]=1
    if company_name in database_keys:
        prev_values=db.child(company_name).get()
        fetching_keys={}

        for i in prev_values.each():
            fetching_keys[i.key()]=1
        #print(fetching_keys)
    st.write("It will be done.....")
    reviews,insta_id,pos,neg,social_media_links,indeed_rating=sentiment_analyse(company_name)
    try:
        total_followers_linkedin,total_count_reaction=linkedin_get(social_media_links["linkedin"])
    except:
        total_followers_linkedin,total_count_reaction=0,0

    number_of_twitter_followers=0
    number_of_twitter_followers=twitter_scrape(social_media_links["twitter"])
    st.write("Company found it")
    #base_value=base_value*10 
    base_value=prev=10.0
    st.write("The Initial base value is {}".format(base_value))
    count=followers_count(insta_id)

 
    if company_name in database_keys:
    #prev_values=db.child(company_name).get()
        fetch_dict=[]
        for i in prev_values.each():
            fetch_dict.append(i.val())
        print(fetch_dict)
        prev=fetch_dict[5]
        base_value=fetch_dict[5]
        if fetch_dict[6]<pos:
            base_value+=0.1
            sending(True)
        if neg>0 and neg>fetch_dict[4]:
            base_value-=0.1 
            sending(False)
        if fetch_dict[0]<count["Followers"]:
            base_value+=0.01
            sending(True,"instagram followers")
        if fetch_dict[0]>count["Followers"]:
            base_value-=0.01
            sending(False,"instagram followers")
        if fetch_dict[2]<total_followers_linkedin:
            base_value+=0.01
            sending(True,"linedin followers")
        if fetch_dict[2]>total_followers_linkedin:
            base_value-=0.01
            sending(False,"linedin followers")
        if fetch_dict[3]<total_count_reaction:
            base_value+=0.001 
            sending(True,"reaction increased")
        if fetch_dict[3]>total_count_reaction:
            base_value-=0.001
            
        if float(fetch_dict[7])>float(number_of_twitter_followers):
            base_value-=0.01
            sending(False,"twitter followers")
        if float(fetch_dict[7])<float(number_of_twitter_followers):
            base_value+=0.01
            sending(True,"twitter followers")
        if fetch_dict[8]>indeed_rating:
            base_value-=0.01 
            sending(False,"indeed rating")
        if fetch_dict[8]<indeed_rating:
            base_value+=0.01 
            sending(True,"indeed rating")

    
    data={"pos_value":pos,'neg_value':neg,"insta_followers":count["Followers"],"new_base":base_value,"insta_id":insta_id,"linkedin_followers":total_followers_linkedin,"linkedin_reaction_count":total_count_reaction,"twitter_followers":number_of_twitter_followers,"under_indeed_rating":indeed_rating,"vunder_reviews":reviews,"zlinks":social_media_links}
    db.child(company_name).set(data)
    if prev!=base_value:
        if prev>base_value:
            sending(False)
        st.write(f"The changes from {prev} to {base_value}")
    else:
        st.write("Done")
        
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .main {background-color: #f8f9d2;
            background-color: #f8f9d2;
background-image: linear-gradient(315deg, #f8f9d2 0%, #e8dbfc 74%);
color:black;
            
            
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)