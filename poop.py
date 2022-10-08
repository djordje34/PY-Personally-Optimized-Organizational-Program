
import collections
import requests
from functions.onlinefuncs import find_my_ip, get_random_joke, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_whatsapp_message
from functions.offlinefuncs import open_calculator, open_cmd, open_notepad, open_vsc, open_discord
from pprint import pprint
from datetime import datetime
import pyttsx3
from decouple import config
import os
import subprocess as sp
import speech_recognition as sr
from random import choice
from functions.utils import opening_text
from PIL import ImageTk, Image
import tkinter.font as font
from tkcalendar import Calendar
import tkinter as tk
from calendarsel import getWindow
color={"purple":"#461E52",
        "pink":"#DD517F",
        "yellow":"#E68E36",
        "darkblue":"#556DC8",
        "lightblue":"#7998EE"}

class Poop():
    
    def __init__(self):
        
        self.BOTNAME = config('BOTNAME')

        self.engine = pyttsx3.init('sapi5')

        self.engine.setProperty('rate', 190)

        self.engine.setProperty('volume', 1.0)

        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)
        self.USERNAME=os.environ.get('USERNAME')
        


    def speak(self,text):
            """speak text/string passed as argument"""
        
            self.engine.say(text)
            self.engine.runAndWait()

    def greet(self):
            """Greets the user according to the time"""

            hour = datetime.now().hour
            returnable=""
            if (hour >= 0) and (hour < 12):
                self.speak(f"Good Morning {self.USERNAME}")
                returnable+="Good Morning"+ self.USERNAME+"\n"
            elif (hour >= 12) and (hour < 18):
                self.speak(f"Good afternoon {self.USERNAME}")
                returnable+="Good afternoon"+ self.USERNAME+"\n"
            elif (hour >= 18) and (hour < 24):
                self.speak(f"Good Evening {self.USERNAME}")
                returnable+="Good Evening"+ self.USERNAME+"\n"
            self.speak(f"My name is {self.BOTNAME}, and I am your Personally Optimized Organizational Program")
            self.speak(f"How may I assist you?")
            returnable+="My name is "+self.BOTNAME+", and I am your Personally Optimized Organizational Program."+"\n"+"How may I assist you?"
            self.greeter=returnable


    def input(self):
            """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

            r = sr.Recognizer()
            with sr.Microphone() as source:
                self.speak("I'm listening")
                r.pause_threshold = 1
                audio = r.listen(source)

            try:
                self.speak(f"I'm processing what you just said {self.USERNAME}")
                query = r.recognize_google(audio, language='en')
                if not 'exit' in query or 'stop' in query:
                    self.speak(choice(opening_text(self.USERNAME)))
                else:
                    hour = datetime.now().hour
                    if hour >= 21 and hour < 6:
                        self.speak(f"Good night {self.USERNAME}, take care!")
                    else:
                        self.speak(f'Have a good day {self.USERNAME}!')
                    exit()
            except Exception:
                self.speak('Sorry, I could not understand. Could you please say that again?')
                query = 'None'
            return query
    
    def talk(self):
        
            
            #global win
            #win.grab_set()
            query = self.input().lower()
            yield query
            #userText["text"]=query
            #userText.pack()
            #win.update()
            #win.grab_set()
            if 'open visual studio code' in query:
                open_vsc()

            elif 'open discord' in query:
                open_discord()

            elif 'open command prompt' in query or 'open cmd' in query:
                open_cmd()


            elif 'open calculator' in query:
                open_calculator()

            elif 'ip address' in query:
                ip_address = find_my_ip()
                self.speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen.')
                yield(f'Your IP Address is {ip_address}')

            elif 'wikipedia' in query:
                self.speak('What do you want to search on Wikipedia?')
                yield("What do you want to search on Wikipedia?")
                search_query = self.input().lower()
                yield(search_query)
                results = search_on_wikipedia(search_query)
                self.speak(f"According to Wikipedia, {results}")
                self.speak("For your convenience, I am printing it on the screen.")
                yield(results)

            elif 'youtube' in query:
                self.speak('What do you want to play on Youtube,?')
                video = self.input().lower()
                yield(video)
                play_on_youtube(video)

            elif 'google' in query:
                self.speak('What do you want to search on Google,?')
                query = self.input().lower()
                search_on_google(query)

            elif "send whatsapp message" in query:
                self.speak('On what number should I send the message? Please enter in the console: ')
                number =input("Enter the number: ")
                self.speak("What is the message?")
                message = self.input().lower()
                send_whatsapp_message(number, message)
                self.speak("I've sent the message.")

           

            elif 'joke' in query:
                self.speak(f"Hope you like this one")
                joke = get_random_joke()
                self.speak(joke)
                self.speak("For your convenience, I am printing it on the screen.")
                yield(joke)


            elif 'weather' in query:
                ip_address = find_my_ip()
                city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
                self.speak(f"Getting weather report for your city {city}")
                weather, temperature, feels_like = get_weather_report(city)
                self.speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
                self.speak(f"Also, the weather report talks about {weather}")
                self.speak("For your convenience, I am printing it on the screen.")
                yield(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
        
            #self.win.mainloop()
            #win.grab_release()
            elif 'note' in query:
                self.speak("What should I write in the Notepad?")
                msg=self.input().lower()
                self.speak("All right! Opening application for notes.")
                self.speak("Please select a date")
                getWindow(msg,self.USERNAME)
def main():                             #NOVA FNKCIJA U GUI DA POZOVE TALK BLOKIRA PROZOR I PRIKAZI LISTENING KAD SE UPALI TALK!!!
    pass
    
if __name__=="__main__":
    main()
    