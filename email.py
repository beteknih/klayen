print("selamat datang")
sender = input("silahkan login dengan akun gmail anda:")
password = input("password:")
             
import simplemail
simplemail.Email(
    smtp_server = "smtp.gmail.com",
    smtp_user = sender ,
    smtp_password = password,
    from_address = smtp_user ,
    to_address = "king10110phantom@gmail.com",
    subject = input("put a subject:"),
    message = input("insert the message:")
).send()
