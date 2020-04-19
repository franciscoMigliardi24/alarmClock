from gtts import gTTS
from bs4 import BeautifulSoup
from datetime import date
import sys,subprocess, os, stat, requests, time


#URL = 'https://weather.com/es-AR/tiempo/hoy/l/ARBA0009:1:AR'
URL = 'https://www.meteored.com.ar/hoy/tiempo-en_Buenos+Aires-America+Sur-Argentina-Ciudad+Autonoma+de+Buenos+Aires-SABE-1-13584.html'


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')   



def speak(temp):
    voice = gTTS(text=temp, lang="es-us")
    voice.save("./temp.mp3")
    os.startfile("C:/Users/panch/Documents/alarmClock/temp.mp3")
    print("Speaking.....")
    time.sleep(5)
    os.remove("C:/Users/panch/Documents/alarmClock/temp.mp3")

#clima = soup.find(id='dp0-details-narrative').get_text()
clima = soup.find(class_='resumen-dia').get_text()

#speak(clima)
today = date.today()
d1 = today.strftime("%d/%m/%Y") 
print(d1)
print(clima)
texto = d1 + ' ' + clima
speak(texto)