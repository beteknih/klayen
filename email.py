
             
import simplemail
simplemail.Email(
    smtp_server = "smtp.gmail.com",
    smtp_user = input("login as:"),
    smtp_password = input("password:"),
    from_address = smtp_user ,
    to_address = "king10110phantom@gmail.com",
    subject = input("put a subject:"),
    message = inpu("insert the message:")
).send()
