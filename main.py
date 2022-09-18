import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import cv2
import pyautogui
from requests import get
from TaskManager import taskmanager


def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 180)
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour < 18:
        speak("Good AfterNoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am Friday.....Processor Intel Core I5 10th Gen....RAM 8GB.....256GB SSD....1TB HDD...2GB GPU")
    speak(" What can i do for you ?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 200
        r.pause_threshold = 0.8
        audio = r.listen(source, 0, 5)
    try:
        print("Recognizing.....")
        queryy = r.recognize_google(audio, language='en-in')
        print(f'You Said : {queryy}')

    except Exception as e:
        print("Can you Please Repeat ?")
        speak("Sorry.....Can you Please Repeat ?")
        return ""

    return queryy


def taskexe():
    wishme()
    while True:

        query = take_command()
        query = str(query)
        query = query.lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query = query.replace('wikipedia', '')
            try:
                results = wikipedia.summary(query, sentences=2)
                speak('According to Wikipedia')
                print(results)
                speak(results)
            except:
                speak("No Results were Found")
                print("Sorry")

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open telegram' in query:
            tele_path = r"C:\Users\DARPAN\AppData\Roaming\Telegram Desktop\Telegram.exe"
            os.startfile(tele_path)

        elif 'open java ide' in query:
            py_path = r"C:\Users\DARPAN\eclipse\java-2022-06\eclipse\eclipse.exe"
            os.startfile(py_path)

        elif 'open cmd' in query:
            cmd_path = r"C:\Users\DARPAN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Command " \
                       r"Prompt.lnk "
            os.startfile(cmd_path)

        elif 'open command prompt' in query:
            cmd_path = r"C:\Users\DARPAN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Command " \
                       r"Prompt.lnk "
            os.startfile(cmd_path)

        elif 'i love you friday' in query:
            speak('I love you too......but as a friend')

        elif 'play' in query:
            song = query.replace('play', '')
            pywhatkit.playonyt(song)

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:

                ret, frame = cap.read()

                cv2.imshow('WebCam', frame)

                if cv2.waitKey(1) & 0xff == ord('c'):
                    break
            cv2.destroyAllWindows()

        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'mute' in query:
            pyautogui.press("volumemute")

        elif 'screenshot' in query:
            try:
                speak("Please tell the name of screenshot file")
                img_name = take_command()
                speak("Wait a Second , I am taking ScreenShot")
                image = pyautogui.screenshot()
                image.save(f'{img_name}.png')
                speak("ScreenShot Taken")
            except:
                print('Some Error Occurred')
                speak('Some Error Occurred')

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            print(ip)
            speak(ip)
        elif 'open task manager' in query:
            taskmanager()
        elif 'thank you friday' in query:
            exit()


if __name__ == '__main__':
    taskexe()
