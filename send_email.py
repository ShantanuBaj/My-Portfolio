import smtplib
import ssl


host= "smtp.gmail.com"
port= 465

username= "shantanu007.sb@gmail.com"
password= "ftuk psdq iaji jikn"

receiver= "shantanu007.sb@gmail.com"

context= ssl.create_default_context()

message= """
Hi!
How are you?"""

with smtplib.SMTP_SSL(host=host,port=port,context=context) as server:
    server.login(username,password)
    server.sendmail(username,receiver,message)