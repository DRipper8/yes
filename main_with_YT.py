from selenium import webdriver
import pyttsx3 as p
import speech_recognition as sr

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 200)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
r = sr.Recognizer()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen(source):
    audio = r.listen(source)
    return r.recognize_google(audio)


class Infowiki:
    def __init__(self):
        self.driver = webdriver.Chrome("C:/Program Files/Google/Chrome/chromedriver_win32/chromedriver.exe")

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element("xpath", '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element("xpath", '//*[@id="search-form"]/fieldset/button')
        enter.click()


class music():
    def __init__(self):
        self.driver = webdriver.Chrome("C:/Program Files/Google/Chrome/chromedriver_win32/chromedriver.exe")

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element("xpath", '//*[@id="video-title"]/yt-formatted-string')
        video.click()


speak("hello sir, how are you today?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    while True:
        print("listening...")
        text = listen(source)
        print(text)
        if all(x in text for x in ["what", "about", "you"]) or all(x in text for x in ["how", "about", "you"]):
            speak("I am very good thank you")
        elif all(x in text for x in ["information", "informations"]):
            speak("you need information to which topic?")
            infor = listen(source)
            speak("one moment i am looking for {} in wikipedia".format(infor))
            assist = Infowiki()
            assist.get_info(infor)
        elif all(x in text for x in ["song"]):
            speak("which song?")
            songname = listen(source)
            speak("one moment im looking for {} on youtube".format(songname))
            print("playing {} on youtube".format(songname))
            assist = music()
            assist.play(songname)

        speak("what can I do for you?")
