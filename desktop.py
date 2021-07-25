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

def shutdown():
    os.system('shutdown /s /t 10')

def restart():
    os.system('shutdown /r /t 10')

def file_manager():
    subprocess.run(["explorer", ","])

def camera():
    subprocess.run('start microsoft.windows.camera:', shell=True)

def email():
    webbrowser.open('mailto:', new=1)

def notepad():
    subprocess.Popen(['notepad.exe'])

def wordpad():
    subprocess.Popen(['write.exe'])

def switch_window():
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    # time.sleep(1)
    pyautogui.keyUp("alt")

def close_current_window():
    pyautogui.keyDown("alt")
    pyautogui.press("F4")
    # time.sleep(1)
    pyautogui.keyUp("alt")

def excel():
    os.system('start excel.exe') 
    
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
    webbrowser.open(url)

def find_files(filename, search_path):
    result = []

    # Wlaking top-down from the root
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result

def voice():
    lines = {
        'hello':'how can i help you sir',
        'hi':'hello robin', 
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

    return sound


if __name__ == "__main__":
    wish()
    while True:
        sound = voice()
        if sound == 'bye' or sound == 'bye bye':
            exit()
        elif  'open camera' in sound:
            camera()
        elif  'switch window' in sound:
            switch_window()
        elif  'close' in sound or 'closing' in sound:
            close_current_window()
        elif 'open files' in sound:
            file_manager()
        elif 'open excel' in sound:
            excel()
        elif 'listen' in sound:
            googlesearch()        
        elif 'shutdown' in sound:
            shutdown()
            close_current_window()
            exit()
        elif 'restart' in sound:
            restart()
            close_current_window()
            exit()

        elif 'open typing master' in sound:
            subprocess.Popen("C:\\Program Files (x86)\\TypingMaster\\tmaster.exe") 
        elif 'open code blocks' in sound:
            subprocess.Popen("C:\\Program Files\\CodeBlocks\\codeblocks.exe")







        # elif 'find file' in sound:
        #     filename = voice()
        #     search_path = "C:"
        #     find_files(filename,search_path)