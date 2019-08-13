import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def wishMe():
  hour = int(datetime.datetime.now().hour)
  if hour>=0 and hour<12:
    speak("Good Morning Sir")

  elif hour>=12 and hour<18:
      speak("Good Afternoon Sir")

  else:
    speak("Good Evening")

  speak("I am Alica.... MISTER NITIIK.... Please tell me how i may help you...")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold =1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that  again please....")
        return "None"
    return query







if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open mozilla firefox' in query:
            webbrowser.open("mozilla.com") 

        elif 'play' in query:
                music_dir = 'G:\\Sounds'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[0]))   
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")  

        elif 'open visual studio code' in query:
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'bye'in query:
            speak("OKAY SIR....... HAVE A GOOD DAY!!!! BYE") 
            sys.exit()

        elif 'how are you' in query:
            stmsg = ['Chilling.....','fine sir....','In your service sir....']
            speak(random.choice(stmsg))

        elif 'NAMASTEE' in query:
            speak("NAMASTEE KIDDAA....")

                 
       
          

   