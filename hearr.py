import speech_recognition as sr
import webbrowser as wb

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


# obtain audio from the microphone  
r = sr.Recognizer()
with sr.Microphone() as source:  
   print("Please wait. Calibrating microphone...")  
   # listen for 5 seconds and create the ambient noise energy level  
   r.adjust_for_ambient_noise(source, duration=5)  
   print("Say something!")  
   audio = r.listen(source)  

# recognize speech 
try:
    text = r.recognize_google(audio, language = 'en-IN', show_all = True )
    print("I thinks you said '" + r.recognize_google(audio) + "'")

    f_text='https://www.google.co.in/search?q=' + text
    wb.get(chrome_path).open(f_text)

    
#except sr.UnknownValueError:  
#  print("I could not understand audio")  
except sr.RequestError as e:  
   print("error; {0}".format(e))

except Exception as e:
   print (e)