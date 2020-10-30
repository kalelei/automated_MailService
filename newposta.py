#https://myaccount.google.com/lesssecureapps?pli=1 fist you should Activate the less secure apps options

#1)Toplu mail
#2)HTML formatına çevir

import glob
import os
import smtplib, ssl, getpass, email

from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject="AN ATTACHMENT EMAİL FROM PYTHON"
body= "This is an email with attachment sent from python"
sender_email="yk.kaleli@gmail.com"
receiver_email=['yk.kaleli@gmail.com'] #Normaly using company mail address
password = getpass.getpass(prompt='Enter password:')

#other=input("Enter another mail adress to sent:::")
#receiver_email.append(other)
print(receiver_email)

##COMMASPACE= ', '

port = 587 # For starttls
smtp_server="smtp.gmail.com"


message=MIMEMultipart()
message["From"] = sender_email
message["To"] = ', '.join(receiver_email)
message["Subject"] = subject
text=MIMEText("DENEME YAZISI")



"""
  #The script file and the document must be in the same dir
img_data = open(filename, 'rb').read()
message.attach(text)                                              #To add image as attachment to mail                          
image = MIMEImage(img_data, name=os.path.basename(filename))
message.attach(image)
"""


for each_file_path in glob.glob('*.txt'):  #Reads all the files one by one
    try:
        file_name=each_file_path.split("/")[-1]
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(each_file_path, "rb").read())

        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment' ,filename=file_name)
        message.attach(part)
    except:
        print ("could not attache file")


#start secure SSL context
context = ssl.create_default_context()
try:
    server=smtplib.SMTP(smtp_server,port)
    server.ehlo()
    server.starttls(context=context) #start tlls
    server.ehlo()
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message.as_string())
except Exception as e:
    print(e)

finally:
    server.quit()
