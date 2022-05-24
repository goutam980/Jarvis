import pyttsx3 as pt

engine=pt.init('sapi5')
voice=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
print(voices[0].id)