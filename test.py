# Databricks notebook source
# import smtplib, ssl
# from email.message import EmailMessage
# from getpass import getpass

# # server = smtplib.SMTP(host='smtp.office365.com', port=587)

# host='smtp.office365.com'

# port = 587

# port = 465  # For SSL

# email = "kunstek.cc@pg.com"
# password = getPass("Type your password and press enter: ")



# msg = EmailMessage()
# msg['From'] = f'{email}'
# msg['Subject'] = 'Some subject here'
# msg['To'] = ', '.join([f'{email}', f'{email}'])

# msg.set_content('Some text here')


# # Create a secure SSL context
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(host, port, context=context) as server:
#     server.login(f"{email}", password)
#     smtp.send_message(msg)
#     print('Email sent!')
#     # TODO: Send email here

# COMMAND ----------

# import smtplib, ssl
# import os smtp_server = "smtp.office365.com"
# port = 587  # For starttls
# sender = 'beghin.ac@pg.com'
# password = os.environ.get('iri_pw') # Create a secure SSL context
# context = ssl.create_default_context()
# message = """\
#     Subject: Hi there     This message is sent from Python.""" # Try to log in to server and send email
# try:
#     server = smtplib.SMTP(smtp_server,port)
#     server.ehlo() # Can be omitted
#     server.starttls() # Secure the connection
#     server.ehlo() # Can be omitted
#     server.login(sender, password)
#     server.sendmail(sender, 'kunstek.cc@pg.com', message)
# except Exception as e:
#     # Print any error messages to stdout
#     print(e)
# finally:
#     server.quit()

# COMMAND ----------

# https://adb-8806507422276424.4.azuredatabricks.net/?o=8806507422276424#notebook/2357256091534847/command/2357256091534868

# COMMAND ----------

from datetime import date
from datetime import datetime
from datetime import timedelta
from statistics import mean
import pandas as pd
import numpy as np
from pyspark.sql import functions as F
from pyspark.sql.window import Window

# COMMAND ----------

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import smtplib
import ssl
from email.message import EmailMessage
from getpass import getpass

# COMMAND ----------

# HOST = "smtp-mail.outlook.com"
# HOST = "smtp.office365.com"
HOST = "smtpgwpub.pg.com"

PORT = "587"
# PORT = "465"

SENDER = "kunstek.cc@pg.com"
RECIPIENT = "kunstek.cc@pg.com"
SUBJECT = "testing"
MSG = "test"

# COMMAND ----------

PASSWORD = getpass("Type your password and press enter: ")

# COMMAND ----------

msg = EmailMessage()
msg['From'] = SENDER
msg['Subject'] = SUBJECT
msg['To'] = [RECIPIENT]
msg.set_content(MSG)

# COMMAND ----------

server = smtplib.SMTP(host=HOST, port=PORT)
server.starttls()
server.login(SENDER, PASSWORD)
server.sendmail(SENDER, [RECIPIENT], MSG)

# COMMAND ----------

# # Create a secure SSL context
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(host, port, context=context) as server:
#     server.login(SENDER, PASSWORD)
#     smtp.send_message(msg)
#     print('Email sent!')

# COMMAND ----------

# server = smtplib.SMTP(host='smtpgwpub.pg.com', port=587)
# server.starttls()

# COMMAND ----------

def send_email(product, email_list):
  
  server = smtplib.SMTP(host='smtpgwpub.pg.com', port=587)
  server.starttls()
  sender = 'samsloyalty.im@pg.com' # the Special ID account you are sending as
  receivers = email_list # your recipients
  msg = MIMEMultipart('alternative')
  text = f"""
  Hello. AUR of item # {product[0]} has increased by {product[3]}% in {product[4]} clubs. Please view this link to check that.
  """
  html = f"""
<html>
  <head></head>
  <body>
    <p>Hello. AUR of item # {product[0]} has increased by {product[3]}% in {product[4]} clubs. Please view this <a href="https://app.powerbi.com/groups/me/apps/41b8dd2d-b4c3-4a27-ac63-4a3251579f5c/reports/127b4891-bbed-4ed6-8895-c809281745aa/ReportSection?ctid=3596192b-fdf5-4e2c-a6fa-acb706c963d8">link</a> to check that.<br>
    </p>
  </body>
</html>
""" 
  password = dbutils.secrets.get(scope = "azurekeyvault_secret_scope", key = "samsloyalty-ION")
  msg['From'] = "samsloyalty.im@pg.com"
  recipients = ', '.join(f'{item}' for item in email_list)
  msg['To'] = recipients
  msg['Subject'] = f"AI Bot Noticed {product[1]} in {product[2]} had an increase in AUR"
  msg.attach(MIMEText(text, 'plain'))
  msg.attach(MIMEText(html, 'html'))
  server.login(sender, password)
  server.sendmail(sender, receivers, msg.as_string())

