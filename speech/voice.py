import pyaudio
import speech_recognition as sr

def sppech_txt():
    r=sr.Recognizer()
    while True:
        with sr.Microphone() as source:  #source=sr.Microphone
            print('speak now....')
            audio=r.listen(source)

            


            try:
                text=r.recognize_google(audio)
                print('your said text:',text)
                if text=='stop':
                    break
            except:
                print('didnt hear anything')


sppech_txt()