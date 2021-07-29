from googlesearch import search
import speech_recognition as sr
import pyttsx3
from pyaudio import *
import os
import subprocess
import webbrowser
import pyautogui
import datetime
import urllib.request
import urllib.parse
import re


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12 :
        pyttsx3.speak('good morning sir')
    elif hour >= 12 and hour < 17 :
        pyttsx3.speak('good afternoon sir')
    elif hour >= 17 and hour < 19 :
        pyttsx3.speak('good evening sir')
    else:
        pyttsx3.speak('good night sir')

def close_current_window():
    pyautogui.hotkey('alt', 'f4')

def googlesearch(): 
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")
    # to search
    pyttsx3.speak('yes sir')
    query = voice()
    
    for url in search(query, tld="com", num=1, stop=1, pause=2):
        pass    
    webbrowser.open_new_tab(url)

def voice():
    lines = {
        'hello':'how can i help you sir',
        'are you listen': 'yes sir' 
    }
    r = sr.Recognizer()

    def speak(sound):
        engine = pyttsx3.init()
        engine.say(sound)
        engine.runAndWait()

    try:
        with sr.Microphone() as source:
            print('listening...')
            r.adjust_for_ambient_noise(source)
            audio2 = r.listen(source)
            print(audio2)
            audio = r.recognize_google(audio2,language='en-IN')
            sound = audio.lower()
            print(sound)          
            for x in lines:
                if x in sound:
                    speak(lines[x])
            return sound
    except Exception as e:
        file = 'say again'
        print(file)
        return file
    

if __name__ == "__main__":
    wish()
    while True:
        sound = voice()
        if sound == 'bye' or sound == 'bye bye':
            pyttsx3.speak('bye have a nice day')
            exit()
        elif  'switch window' in sound:
            pyautogui.hotkey('alt','tab')
        elif  'select all' in sound:
            pyautogui.hotkey('ctrl','a')
        elif  'copy' in sound:
            pyautogui.hotkey('ctrl','c')
        elif  'paste' in sound:
            pyautogui.hotkey('ctrl','v')
        elif  'save' in sound:
            pyautogui.hotkey('ctrl','s')
        elif 'enter' in sound:
            pyautogui.press('enter')
        elif  'close' in sound or 'closing' in sound:
            close_current_window()
        elif 'open files' in sound:
            subprocess.run(["explorer", ","])
        elif  'open camera' in sound:
            subprocess.run('start microsoft.windows.camera:', shell=True)
        elif 'take screenshot' in sound:
            pyautogui.hotkey('win','prtscr')
        elif 'open excel' in sound:
            os.system('start excel.exe')
        elif 'open notepad' in sound:
            subprocess.Popen(['notepad.exe'])
        elif 'listen' in sound:
            googlesearch()        
        elif 'shutdown' in sound:
            os.system('shutdown /s /t 10')
            close_current_window()
            exit()
        elif 'restart' in sound:
            os.system('shutdown /r /t 10')
            close_current_window()
            exit()
        # elif 'open typing master' in sound:
        #     subprocess.Popen("C:\\Program Files (x86)\\TypingMaster\\tmaster.exe") 
        # elif 'open code blocks' in sound:
        #     subprocess.Popen("C:\\Program Files\\CodeBlocks\\codeblocks.exe")
