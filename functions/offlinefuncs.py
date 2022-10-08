from datetime import datetime
import os
import subprocess as sp
import speech_recognition as sr
from random import choice



username=os.environ.get('USERNAME')
paths = {
    'vsc': "E:\\Users\\"+username+"\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    'discord': "C:\\Users\\"+username+"\\AppData\\Local\Discord\\app-1.0.9006\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


    
def open_vsc():
        os.startfile(paths['vsc'])


def open_discord():
        os.startfile(paths['discord'])
        
def open_cmd():
        os.system('start cmd')
        
def open_calculator():
        sp.Popen(paths['calculator'])
        
def open_notepad(file):
        os.startfile(file)
def main():
    open_vsc()

if __name__=="__main__":
    main()