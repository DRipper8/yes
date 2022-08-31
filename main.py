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


speak("hello sir, how are you today?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    while True:
        print("listening...")
        text = listen(source)
        print(text)
        if "what" and "about" and "you" or "how" and "about" and "you" in text:
            speak("I am very good thank you")
        elif "information" in text:
            speak("you need information to which topic?")
            infor = listen(source)
            speak("one moment i am looking for {} in wikipedia".format(infor))
            assist = Infowiki()
            assist.get_info(infor)

        speak("what can I do for you?")
