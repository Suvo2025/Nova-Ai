import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from google import genai
from gtts import gTTS
import pygame
import os
from client import aiProcess


recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi = "12beb982afc34296967a77cf6d19bc08"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()


def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 




def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles[:5]:
                speak(article['title'])
    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output)       

if __name__=="__main__":
    speak("Initializing Nova.... ")
    while True:
        r=sr.Recognizer()
        

        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening!....")
                audio=r.listen(source,timeout=3,phrase_time_limit=5)
            word=r.recognize_google(audio)
            if "nova" in word.lower():
                speak("Yes?")

                with sr.Microphone() as source:
                    print("Nova Active....")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("error: {0}".format(e))