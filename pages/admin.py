import pyrebase
import pandas as pd 
import streamlit as st 
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
firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()
db=firebase.database()
database_keys={}


def login():
    email=st.text_input("Enter your email")
    login_sucessfull=False
    password=st.text_input("Enter your password")
    if email!="" and password!="":
        try:
            login=auth.sign_in_with_email_and_password(email,password)
            
            login_sucessfull=True 
           
        except:
            st.write("invalid")
    else:
        st.error("Empty values can't be entered")
    return login_sucessfull
login_done=login()
 
if login_done==True:

    x=[]
    for j in db.get():
        x.append(j.key())
    option = st.selectbox(
     'Select it',x)    
    value=""
    for j in db.get():
        if option==j.key():
            value=j.val()

    st.write(value)

