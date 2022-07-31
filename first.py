import playsound
import speech_recognition as sr
from gtts import gTTS 
from bitstring import BitArray
from os import path
from pydub import AudioSegment

#def speak(text):
r = sr.Recognizer()  
with sr.Microphone() as source:
    tts = gTTS(text="Please wait. Calibrating microphone ", lang="en") 
    filename = "voice1.mp3"
    tts.save(filename)
    playsound.playsound(filename) 
    print("Please wait. Calibrating microphone...")  
     # listen for 5 seconds and create the ambient noise energy level  
    r.adjust_for_ambient_noise(source, duration=3)  
    print("Say something!")  
    audio = r.listen(source) 

    try:
        str = r.recognize_google(audio)
        tts = gTTS(text=str, lang="en")
        filename = "voice.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        dst = "test.wav"
        # convert wav to mp3                                                            
        sound = AudioSegment.from_mp3(filename)
        sound.export(dst, format="wav")
        

    except Exception as e:
        print("exception: "+ str(e))
        
#speak("hello")


#file = open('first.txt', "r").read()


#converting binary
#b=BitArray(bytes=open('voice.wav','rb').read())

# Store result
#with open('filename_bits.txt', 'w') as file1: 
    #file1.write(b.bin)
    #file1.close()

