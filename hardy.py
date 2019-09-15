import pyttsx3
import datetime
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")  
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("Good evening!")
    speak("I am  Hardy sir !.. How can i help you. ")

def takeCommand():
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
        #print(e)

        print("Sorry..!! Can you please say that again")
        return "None"
    return query


if __name__  == "__main__":
    wishme()
    takeCommand()

