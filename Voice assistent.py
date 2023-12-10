import pyttsx3
from random import choice

engine = pyttsx3.init()

def talk(text):
    print('', text)
    engine.say(text)
    engine.runAndWait()


userName = ''

while True:
    
    st = input('-->: ')
    st = st.lower()

    if st in ['hello','good morning']:
        talk(choice(['Hello!','hi!', 'Good morning!']))

    if st in ['what is your name', 'your name']:
        talk('My name is R2D2!What is your name?')
        userName = input()
        talk('Nice to meet you ' + userName + '!')

    if st in ['bye', 'goodbye'] :
        break

talk('Goodbye! '+ userName)  
