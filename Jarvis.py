import speech_recognition as sr
import pyaudio
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import os
from pytube import YouTube
from speedtest import Speedtest
import getpass
import smtplib

engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        r.pause_threshold=0.5
        audio=r.listen(source)
        
        
    try:
        print('Recognizing...')
        command=r.recognize_google(audio,language='en-in')
        print('You said: '+command)
        
    except Exception as e:
        print(e)
        speak("Please say it again")
        return "None"
    return command

def sendEmail(to,content):
    email=getpass.getpass('email')
    password=getpass.getpass("password")
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(email,password)
    server.sendmail(email,to,content)
    server.close()
    
    
    
def greet():
    
    jarvis=(' i M jarvis sir, how can i help u?')
    
    clock=int(datetime.datetime.now().hour)
    if clock>=0 and clock<=3:
        speak("good midnight"+jarvis)
        
    elif clock>=4 and clock<=11:
        speak("good morning"+jarvis)
        
    elif clock>=12 and clock<=15:
        speak("good afternoon"+jarvis)
        
    elif clock>=16 and clock<=19:
        speak("good evening"+jarvis)
        
    else:
        speak("good night"+jarvis)       

if __name__=='__main__':
    greet()
    while True:

        command=takecommand().lower()

        #Logic behind jarvis

        if "wikipedia" in command:
            speak("searching in wikipedia")
            command=command.replace('wikipedia','')
            text=wikipedia.summary(command,sentences=2)
            print("according to wikipedia:\n"+text)
            speak("according to wikipedia"+text)

        elif 'google' in command:
            pywhatkit.search(command)
            speak('searching in google')

        elif "who are you"in command:
            speak("hi i m jarvis,ur personal assistant ,jarvis stands for Just A Rather Very Intelligent System thank you ")
        
        elif 'youtube' in command:
            song=command.replace('youtube','')
            pywhatkit.playonyt(song)
            print('playing on YouTube:')

        elif 'current time' in command:
            time=datetime.datetime.now().strftime('%I:%M:%p.') 
            print(f'The current time is :{time}')

        elif 'shutdown' in command:
            speak('shutting down the computer')
            os.system("shutdown /s /t 30")

        elif "video download" in command:
            link=input("Enter the link:")
            video=YouTube(link)
            video_q=video.streams.get_highest_resolution()
            path=input("Enter the path:")
            print("downloding...")
            video_q.download(path)

        elif "network speed" in command:
            st=Speedtest()
            print('****************')
            print("download speed:{a} Mbps".format(a=st.download()))
            print("****************")
            print("upload speed:{b} Mbps".format(b=st.upload()))
            print("****************")
            
        elif "show best server" in command:
            st=Speedtest()
            best_server=st.get_best_server()
            for key,value in best_server.items():
                print(key, " : ",value)
        	
        elif 'send mail' in command:
            try:
                speak('what should i send?')
                content=takecommand().capitalize()
                print(content)
                to=input('enter To address:')
                sendEmail(to,content)
                speak('the email has been sent')
                print("the Email has be send successfully!")
            except Exception as e:
                print(e)
                speak('sorry! unable to send mail')
                
        elif "exit"  in command:
            speak("goodbye! have a great day sir")
            exit()
