import datetime
import os
import sys
import time
import webbrowser as wb
import pywhatkit
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
from webdriver_manager.chrome import ChromeDriverManager

language = 'en'
#path = ChromeDriverManager().install()
wikipedia.set_lang('en')
dino = pyttsx3.init()
voices = dino.getProperty('voices')
dino.setProperty('voice', voices[1].id)


def speak(audio):
    print('Dino: ' + audio)
    dino.say(audio)
    dino.runAndWait()


def get_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Panda: ", end='')
        audio = r.listen(source, phrase_time_limit=10)
    try:
        text = r.recognize_google(audio, language='en-US')
        print("" + text)
    except sr.UnknownValueError:
        print('Sorry! I didn\'t get that! Try typing the command!')
        text = str(input('Your order is: '))
    return text
    time.sleep(2)


def welcome():
    # Chao hoi
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening")
    speak("How can i help you?")
    time.sleep(2)


def open_google():
    speak("What should you search")
    search = get_voice().lower()
    url = f"https://google.com/search?q={search}"
    wb.get().open(url)
    speak(f'Here is your {search} on google')
    time.sleep(5)


def open_youtube():
    speak("What should you search")
    search = get_voice().lower()
    url = f"https://youtube.com/search?q={search}"
    wb.get().open(url)
    speak(f'Here is your {search} on youtube')
    time.sleep(5)

def open_video():
    speak("What should you search?")
    search = get_voice().lower()
    pywhatkit.playonyt(search)
    speak(f"Here is your {search} on YouTube.")

def weather():
    speak("Where do you want to see the weather")
    time.sleep(3)
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = get_voice()
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temp = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        sun_time = data["sys"]
        sun_rise = datetime.datetime.fromtimestamp(sun_time["sunrise"])
        sun_set = datetime.datetime.fromtimestamp(sun_time["sunset"])
        wther = data["weather"]
        weather_des = wther[0]["description"]
        now = datetime.datetime.now()
        content = """
        Today is {day} {month} {year}
        The sun rises at {hourrise} hour {minrise} minutes
        The sun sets at  {hourset} hour {minset} minutes
        Average temperature is {temp} ℃
        The air pressure is {pressure} Hectopascal
        Humidity is {humidity}%
        """.format(day=now.day, month=now.month, year=now.year,
                   hourrise=sun_rise.hour,
                   minrise=sun_rise.minute,
                   hourset=sun_set.hour, minset=sun_set.minute,
                   temp=current_temp, pressure=current_pressure,
                   humidity=current_humidity)
        speak(content)
        time.sleep(10)
    else:
        speak("I can't find the city!")


def get_time():
    now = datetime.datetime.now().strftime("%I:%M:%p")
    speak("It's" + now)
    time.sleep(5)


def get_today():
    now = datetime.datetime.now()
    speak("Today is %d  %d" % (now.day, now.month))
    time.sleep(5)


def help():
    speak("""I can:
    1. Search Google
    2. Search YouTube
    3. Play video on Youtube
    4. Open App
    5. Notice date and time
    6. Weather Forecast
    7. Find Definition
    8. Update Covid-19
     """)
    time.sleep(20)


def open_application():
    speak("Which app do you want to open?")
    app = get_voice()
    if "Google" in app:
        speak("Open Google Chrome")
        os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
    elif "microsoft edge" in app:
        speak("Open MicroSoft Edge")
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk")
    elif "word" in app:
        speak("Open Microsoft Word")
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")
    elif "excel" in app:
        speak("Mở Microsoft Excel")
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk")
    elif "powerpoint" in app:
        speak("Mở Microsoft PowerPoint")
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk")
    else:
        speak("App is not installed")
    time.sleep(5)

def tell_me():
    try:
        speak("What do you want to hear about?")
        text = get_voice()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0])
        time.sleep(20)
        for content in contents[1:]:
            speak("Do you want to hear more?")
            ans = get_voice()
            if "No" in ans:
                break
            speak(content)
            time.sleep(20)

        speak("Thank you!")
    except:
        speak("I can't hear")


def stop():
    speak("See you again!")
    sys.exit(0)


def update():
    url = "https://api.covid19api.com/summary"

    try:
        response = requests.get(url)
        data = response.json()

        global_cases = data["Global"]["TotalConfirmed"]
        global_deaths = data["Global"]["TotalDeaths"]
        global_recovered = data["Global"]["TotalRecovered"]
        speak(f"Total Case is {global_cases}\n"
              f"Total Death is {global_deaths}\n"
              f"Total Recovered is {global_recovered}")

    except requests.exceptions.RequestException as e:
        print("An error occurred, please try again", e)
    time.sleep(3)


if __name__ == "__main__":
    welcome()


    def run():
        while True:
            query = get_voice().lower()
            if "google" in query:
                open_google()
            elif "youtube" in query:
                open_youtube()
            elif "stop" in query:
                speak("Dino is off.Goodbye!")
                stop()
            elif "weather" in query:
                weather()
            elif "time" in query:
                get_time()
            elif "today" in query:
                get_today()
            elif "help" in query:
                help()
            elif "open app" in query:
                open_application()
            elif "tell me" in query:
                tell_me()
            elif "covid" in query:
                update()
            elif "open video" in query:
                open_video()
            else:
                speak("I don't understand or don't have that function please try another sentence")
                return run()


    run()
