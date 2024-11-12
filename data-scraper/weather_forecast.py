import os
import requests
from dotenv import load_dotenv
import send_email
import cron_manager

load_dotenv()

OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
OPEN_WEATHER_API_URL = os.getenv("OPEN_WEATHER_API_URL")
CITY_NAME = os.getenv("CITY_NAME")

units="metric"
url= f"{OPEN_WEATHER_API_URL}?q={CITY_NAME}&appid={OPEN_WEATHER_API_KEY}&units={units}"

resp = requests.get(url)

data = resp.json()

def check_weather():
  if resp.status_code == 200:
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    return temp, description, humidity
  else:
    print("API request error")
    return None

def gen_report():
  temp, description, humidity = check_weather()
  report = f"Temp: {temp}°C, {description}, humidity: {humidity}%"

  with open("weather_report.txt", "w+", encoding="utf-8") as report_file:
    report_file.write(report)

  print("Report generated")

  send_email.send_weather_report_email(city=CITY_NAME, report=report)

  print(report)

cron_manager.start_cron_job(gen_report, 13, 48)
