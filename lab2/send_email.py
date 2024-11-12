import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

PG = os.getenv("PG")
URL = os.getenv("URL")
EMAIL = os.getenv("EMAIL")

def send_email(subject, html_body):
  msg = MIMEMultipart('alternative')
  msg['Subject'] = subject
  msg['From'] = EMAIL
  msg['To'] = EMAIL
  
  msg.attach(MIMEText(html_body, 'html'))
  
  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server_smtp:
    server_smtp.login(EMAIL, PG)
    server_smtp.sendmail(EMAIL, EMAIL, msg.as_string())
    server_smtp.quit()
  
  print("Email sent")

def send_price_alert_email(phone_model, price, rating):
  html_body = f"""\
  <html>
    <head></head>
    <body style="color: #2c3e50; font-family: sans-serif;">
      <h1 style="font-size: 24px">
        💸 Price alert
      </h1>
      <p style="font-size: 16px;">
        Price for
        <strong>{phone_model}</strong>
        is now
        <strong style="color: #27ae60;">{price} Lei</strong>
      </p>
      <p>Rating: {"⭐" * int(rating.split(".")[0])} {rating}</p>
      <p class="margin-top: 20px;">🔗 Link: {URL}</p>
    </body>
  </html>
  """
  
  send_email(subject="Price alert " + phone_model, html_body=html_body)

def send_weather_report_email(city, report):
  html_body = f"""\
  <html>
    <head></head>
    <body style="color: #2c3e50; font-family: sans-serif;">
      <h1 style="font-size: 24px">
        Weather report: {city}
      </h1>
      <p style="font-size: 16px;">
        {report}
      </p>
    </body>
  </html>
  """

  send_email(subject=f"Weather report for {city}", html_body=html_body)
