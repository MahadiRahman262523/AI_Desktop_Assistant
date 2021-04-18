import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
#from django.contrib.gis.gdal.raster import source


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said : {query}")

    except Exception as e:
        speak("Say That Again Please...")
        return "none"
    return query


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour > 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('mahadirahman262523@gmail.com', 'mrd_srs_26_25_23_11_8_10')
    server.sendmail('mahadirahman262523@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    #speak("Hi Mahadi Rahman Dhrubo")
    wish()
    # if 1:
    while True:
        query = takecommand().lower()

        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open adobe reader" in query:
            apath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "E:\\Audio"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP Address is {ip}")

        elif 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("https://stackoverflow.com//")

        elif "open google" in query:
            speak("sir, what should I search on google..")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+880 1954431549", "Hey srtk", 2, 25)

        elif "play songs on youtube" in query:
            kit.playonyt("see you again")

        elif "open whatsapp" in query:
            wpath = "C:\\Users\\ASUS\\AppData\\Local\\WhatsApp"
            os.startfile(wpath)    

        elif "email to rahman" in query:
            try:
                speak("What Should I Say..?")
                content = takecommand().lower()
                to = 'mahadirahman262523@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent to rahman")

            except Exception as e:
                print("sorry sir, I am not able to sent this mail to mrd")

        elif "no thanks" in query:
            speak("Thanks for using me sir. Have a Good Day.")
            sys.exit()

        speak("Sir, Do You Have Any Other Work...??")
