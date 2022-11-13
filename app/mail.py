import smtplib
import os
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import *
import datetime
import csv
import glob
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
user = 'myselfac9@gmail.com'
password = 'rmdu iedn vnfe ezrv'

msg = EmailMessage()
msg['Subject'] = "Private data"
msg['From'] = user
msg['To'] = 'myselfac9@gmail.com'

msg.set_content("There is an csv attached")

user = 'myselfac9@gmail.com'
password = 'rmdu iedn vnfe ezrv'

dd = format(datetime.date.today())


# path = f"D:/webapp/project/media/csv/{dd}.csv"

# with open(path, 'rb') as f:
#     x = f.read()
#     print("binary data", f)
#     xn = f.name
#     print("binary file name", xn)
#     msg.add_attachment(x, maintype='application', subtype='csv', filename=xn)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(user=user, password=password)

    smtp.send_message(msg)
print("ignore errors")
