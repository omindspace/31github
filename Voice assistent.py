import pyttsx3
import speech_recognition as sr
from random import choice

engine = pyttsx3.init()
r = sr.Recognizer()

def talk(text):
    print('', text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as sourse:
        print('Speak...')

        r.adjust_for_ambient_noise(sourse)
        audio = r.listen(sourse)

        try:
            text = r.recognize_google(audio, language="en-En")
        except sr.UnknownValueError:
            pass
        print(text.capitalize())

        return text
userName = ''

while True:
    
    st = listen()
    st = st.lower()

    if st in ['hello','good morning']:
        talk(choice(['Hello!','hi!', 'Good morning!']))

    if st in ['what is your name', 'your name']:
        talk('My name is R2D2!What is your name?')
        userName = listen()
        talk('Nice to meet you ' + userName + '!')

    if st in ['bye', 'goodbye'] :
        break

talk('Goodbye! '+ userName)  
