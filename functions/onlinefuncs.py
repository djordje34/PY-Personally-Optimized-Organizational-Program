import random
import sys
import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

try:
    OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")
except:
    OPENWEATHER_APP_ID=-1

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]


def search_on_wikipedia(query):
    #results = wikipedia.summary(query, sentences=2)
    #return results


    try:
        results = wikipedia.summary(query, sentences=2,auto_suggest=False)
    except wikipedia.DisambiguationError as e:
        print(e.options)
        results = e.options[0]
    print(query)
    print(results)
    return results


def play_on_youtube(video):
    kit.playonyt(video)
    
    
def search_on_google(query):
    kit.search(query)
    
    
    
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+381{number}", message)
    
    
    #NEWS AND EMAIL

def get_weather_report(city):
    if OPENWEATHER_APP_ID==-1:
        sys.exit("OPEN WEATHER APP ID MUST BE SET IN THE .ENV FILE")
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


