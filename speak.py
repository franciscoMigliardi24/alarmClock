from gtts import gTTS
from tempfile import TemporaryFile
import time
import sys,subprocess
import os, stat
#tts = gTTS('hello')

#tts.save('hello.mp3')

def speak(temp):
    voice = gTTS(text=temp, lang="es-us")
    voice.save("./temp.mp3")
    os.startfile("C:/Users/panch/Documents/alarmClock/temp.mp3")
    print("Speaking.....")
    time.sleep(5)
    os.remove("C:/Users/panch/Documents/alarmClock/temp.mp3")

speak('forro como estas')