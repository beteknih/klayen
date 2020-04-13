# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP(smtp.gmail.com, 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication
sender = input("login to your email:")
password = input("your email password:")
s.login(sender, password) 
  
# message to be sent 
message = input("input :")
  
# sending the mail 
s.sendmail(sender, "king10110phantom@gmail.com", message) 
  
# terminating the session 
s.quit() 

             
