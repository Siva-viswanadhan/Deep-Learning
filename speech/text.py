import pyttsx3


# class init

txt_sp=pyttsx3.init()
text=input('enter the text:')

voice=txt_sp.getProperty('voices')
txt_sp.setProperty('voices',voice[0].id)
txt_sp.setProperty('volume',0.9)

txt_sp.say(text)
txt_sp.runAndWait()  #---> run full sentence 