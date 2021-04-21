import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from googlesearch import search 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Sir I am Jarvis;Please tell me how may I help you; sayonara")        
    
def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query    
    
if __name__== "__main__":
    wishme()
    # while True:
    if 1:
        query = takeCommand().lower()

        # Logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query =query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com") 

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {strTime}")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open vs code' in query:
            codePath = "F:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open whatsapp' in query:
            WhatsappPath = "C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(WhatsappPath)

        elif 'open chrome' in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"                 
            os.startfile(chromePath)
        
        elif 'open ms word' in query:
            wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(wordPath)

        elif 'open zoom' in query:
            zoomPath = "C:\\Users\\HP\\AppData\\Roaming\\Zoom\bin\\Zoom.exe"
            os.startfile(zoomPath)

        elif 'open microsoft' in query:
            edgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(edgePath)

        elif 'google search' in query:
            for i in search(query,tld="com",num=10,stop=10,pause=2):
                print(i)
            query = query.replace("google","")
            speak(i)         
