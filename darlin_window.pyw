import sys
import os
from PySide2 import QtCore, QtGui, QtWidgets
from gui import Ui_Dialog
import speech_recognition as sr
import time
import pyttsx3
import datetime
import requests 
from bs4 import BeautifulSoup
import pyowm
from pyowm.commons.enums import SubscriptionTypeEnum
from pyowm.utils.measurables import kelvin_to_celsius
import webbrowser
from threading import Thread

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

def speak(what):
    speak_engine.say(what)
    ui.textEdit.append(what)
    speak_engine.runAndWait()
    speak_engine.stop()

def command():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        speak("Дарлин слушает говорите!")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        zadanie = r.recognize_google(audio, language = "ru-RU").lower()
        speak("Распознано: " + zadanie)
    except sr.UnknownValueError:
        speak("Голос не распознан!")
        zadanie = command()
        
    return zadanie

def execute_cmd(zadanie):
    if zadanie == 'время':
        speak("Уже выполняю!")
        now = datetime.datetime.now()
        speak("Сейчас: " + str(now.hour) + ":" + str(now.minute))
    elif zadanie == 'дата':
        speak("Уже выполняю!")
        now = datetime.datetime.now()
        speak("Сегодня: " + str(now.day) + "." + str(now.month) +"."+ str(now.year))
    elif zadanie == 'новости':
        speak("Вы должны сказать количество новостей")
        zadanie = command()
        number = zadanie
        NEWS = 'https://www.rbc.ua/'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
        full_page = requests.get(NEWS, headers=headers)
        soup = BeautifulSoup(full_page.content,'html.parser')
        convert = soup.findAll("a",{"class": "news-feed-item-heading"}) 
        for i in range(int(number)):
            speak(convert[i].text)
    elif zadanie == 'Paint':
        speak("Уже выполняю!")
        os.system('mspaint')
    elif zadanie == 'блокнот':
        speak("Уже выполняю!")
        os.system('notepad')
    elif zadanie == 'выход':
        speak("Досвидания!")
        exit()
    elif zadanie == 'калькулятор':
        speak("Уже выполняю!")
        os.system('calc')
    elif zadanie == 'выключить пк':
        speak("Выключение будет выполнено через одну минуту!")
        os.system('shutdown /s /t 60')
    elif zadanie == 'погода':
        speak("Вы должны сказать ваш город")
        zadanie = command()
        city = zadanie
        config = {
        'subscription_type': SubscriptionTypeEnum.FREE,
        'language': 'ru',
        'connection': {
        'use_ssl': True,
        'verify_ssl_certs': True,
        'use_proxy': False,
        'timeout_secs': 5
        }
        }
        owm = pyowm.OWM('31428fa04b29e7ca8beb77c718992cec', config=config)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        w = observation.weather
        speak("В городе " + city + " сейчас температура: " + str(kelvin_to_celsius(w.temp['temp'])) + " По Цельсию")
        speak("В городе " + observation.location.name + " сейчас: "+ w.detailed_status )
    elif zadanie == 'поиск':
        speak("Вы должны сказать что хотите найти")
        zadanie = command()
        search = zadanie
        webbrowser.open_new_tab('https://google.com/search?q=' + str(search))
    elif zadanie == 'поиск видео':
        speak("Вы должны сказать что хотите найти")
        zadanie = command()
        search = zadanie
        webbrowser.open_new_tab('https://youtube.com/results?search_query=' + str(search))
    else:
        speak("Разработчик меня еще такому не научил")

speak_engine = pyttsx3.init()
def zapusk():
    while True:
        execute_cmd(command())


thread1 = Thread(target = Ui_Dialog)
thread1.start()
def trade2():
    thread2 = Thread(target = zapusk)
    thread2.start()

def exit_gui():
    exit()
thread3 = Thread(target = exit_gui)
thread3.start()
ui.pushButton_2.clicked.connect(trade2)
ui.pushButton.clicked.connect(exit_gui)
sys.exit(app.exec_())
