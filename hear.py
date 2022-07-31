import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS 

#def speak(text):
r = sr.Recognizer()  
with sr.Microphone() as source:  
    print("Please wait. Calibrating microphone...")  
     # listen for 5 seconds and create the ambient noise energy level  
    r.adjust_for_ambient_noise(source, duration=5)  
    print("Say something!")  
    audio = r.listen(source) 
        

    try:
        text = r.recognize_google(audio, language = 'en-IN', show_all = True )
        print(text)
        print("I thinks you said '" + r.recognize_google(audio) + "'")
        str = r.recognize_google(audio)
        res = ''.join(format(i, '08b') for i in bytearray(str, encoding ='utf-8'))
        print(res)

    except Exception as e:
        print("exception: "+ str(e))
        