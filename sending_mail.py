"""
This code defines a function named sending that sends an 
email using the Simple Mail Transfer Protocol (SMTP) through a Gmail account
The function takes two parameters, s and x, with s presumably representing some condition related to the rating (it's unclear from the code), and x being an optional parameter that defaults to None.

The function then checks if x is None and sets it to the string "to" if it is.

It checks if s is False. If it is, it sets the subject and text of the email for the case of rating decrease. If s is not False, it sets the subject and text for the case of rating increase.

The message variable is constructed with the subject and text.

s.sendmail("hrithikpaul2001@gmail.com", "hrithik26032001.jisu.cse@gmail.com", message): Sends the email using the sendmail method. The sender's email address is "hrithikpaul2001@gmail.com", and the recipient's email address is "hrithik26032001.jisu.cse@gmail.com".

s.quit(): Terminates the SMTP session.


"""

def sending(good_or_bad,reason=None):
    import smtplib
    
    # creates SMTP session
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    
    # start TLS for security
    smtp.starttls()
    
    # Authentication
    smtp.login("hrithikpaul2001@gmail.com", "zwut lzch afvu iswt")
    
    # message to be sent
    if reason==None:
        reason="to"
    if good_or_bad==False:
        SUBJECT = "Rating decreases"   
        TEXT = f"The rating has been decreased due to {reason}, bad comments or reviews or constantly followers decreasing"
    if good_or_bad==True:
        SUBJECT = "Rating increases"   
        TEXT = f"The rating has been increased due to {reason}, good comments or reviews or constantly followers increasing"
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    # sending the mail
    smtp.sendmail("hrithikpaul2001@gmail.com", "hrithik26032001.jisu.cse@gmail.com", message)
    
    # terminating the session
    smtp.quit()

