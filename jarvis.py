import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os # for music
import smtplib # to send mail via gmail

engine = pyttsx3.init('sapi5') #Microsoft's Speech API. We use this to take voices. Windows has in-built voice.
voices = engine.getProperty('voices')
#print(voices[1].id) # prints voices id we see two voices i.e. M and F
engine.setProperty('voice', voices[0].id) # to set voice property

def speak(audio):   #Firstly AI speaks argument i.e. audio
    engine.say(audio) # it says audio string.
    engine.runAndWait() # it runs speak function

def wishMe(): # it wish me
    hour = int(datetime.datetime.now().hour)   # we get hour from 0 to 24 and we typecast it in int
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")

    speak("I am Jarvis sir. Please tell me How may I help you?")

def takeCommand():
    # It takes microphone input from the user and returns string output.

    r = sr.Recognizer() # Recognizer is a class which helps me to recognize the audio
    with sr.Microphone() as source:
        print("Listening...") # we get to know about that it is listening.
        r.pause_threshold = 0.5 # seconds of non-speaking audio before a phrase is considered complete so we take here 0.5 second 
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...") # it recognize the command
        query = r.recognize_google(audio, language='en-in') # we use google's engine here
        #speak(query)
        print(f"User said: {query}\n") # F-strings provide a concise and convenient way to embed python expressions inside string literals for formatting.

    except Exception as e:
        #print(e) # it prints error in console
        print("Say that again please...")
        return "None" # we return None string here it error is there
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email', 'password')
    server.sendmail('email', to, content)
    server.close()

if __name__ == "__main__": # main method for test
    wishMe() # we call wishMe function
    while True:
        query = takeCommand().lower() # convert to lowercase string because query can have capital letters which can cause errors

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "") # to replace query which contain wikipedia to blank
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query: # so how we open youtube so we install inbuilt web browser module
            #webbrowser.open('youtube.com') it opens IE by default
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open('youtube.com')
        
        elif 'open google' in query:
            #webbrowser.open('google.com')
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open('google.com')

        elif 'play music' in query:
            music_dir = 'D://Music'
            songs = os.listdir(music_dir) # list the files of this directory
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0])) # we can use random module 0 to len of songs - 1

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}\n") 

        elif 'open chrome' in query:
            GCPath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
            os.startfile(GCPath)

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "email here"
                sendEmail(to, content)
                speak("Email has benn sent!")
            except Exception as e:
                speak("Sorry, I am not able send this email.")

        elif 'goodbye' in query: 
            speak("Thank you sir!") 
            exit()

        elif 'laugh' in query:
            speak("Have you lost your mind. I can't laugh...")

  


        
