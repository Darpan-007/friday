import pyttsx3
import speech_recognition as sr
from win10toast import ToastNotifier


def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 180)
    engine.say(audio)
    engine.runAndWait()


def take_command():
    speak("What is the Password")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 300
        r.pause_threshold = 0.8
        audio = r.listen(source, 0, 4)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')


    except Exception as e:
        print("Can you Please Repeat ?")
        speak("Can you Please Repeat ?")
        return take_command()

    return query


if __name__ == '__main__':
    print("Virtual Assistant is Password Protected")
    speak("Virtual Assistant is Password Protected")
    print("You must Provide Password To access the Assistant")
    speak("You must Provide Password To access the Assistant")
    password = take_command().lower()

    passwrd = ('yeah dil maange more','yeh dil maange more','dil maange more')

    if password in passwrd:
        notify = ToastNotifier()
        notify.show_toast("FRIDAY","FRIDAY is now Active",threaded=True)
        import main
        main.taskexe()
    else:
        print("Access Denied")
        speak("Alert!..Access Denied")
