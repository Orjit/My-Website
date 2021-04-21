import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser
import os
from googlesearch import search 
import smtplib

print("initializing Ella")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning Orjit")

    elif hour>=12 and hour<16:
        speak("Good Afternoon Orjit")

    else:
        speak("Good Evening Orjit")

    speak("Hey my love What do yu need")            

def takeCommand():
    # It takes microphone input from the user and returns string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshhold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

speak("Initializing Ella")
wishMe()
query = takeCommand().lower()

if 'wikipedia' in query:
    speak('Searching wikipedia...')
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query, sentences =5)
    print(results)
    speak(results)

elif 'google search' in query:
    for i in search(query,tld="com",num=10,stop=10,pause=2):
        print(i)
    query = query.replace("google","")
    speak(i)    
