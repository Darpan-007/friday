import datetime
import pyttsx3
import speech_recognition as sr
from win10toast import ToastNotifier


def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 170)
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 300
        r.pause_threshold = 0.8
        audio = r.listen(source, 0, 5)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f'You Said : {query}')

    except Exception as e:
        print("Can you Please Repeat ?")
        speak("Can you Please Repeat ?")
        return take_command()

    return query


lst_of_task = []


def taskmanager():
    print("What do want to perform")
    speak("What do want to perform")
    print('''
    1. Add a task
    2. View
    3. Delete or Mark_Done
    ''')
    inp_task = take_command().lower()

    if 'add' in inp_task:
        speak('Add a Task')
        new_task = take_command().lower()
        lst_of_task.append(new_task)
        print("Task Manager Updated")

    elif 'view' in inp_task:
        speak('Your Today\'s Task are')
        print(lst_of_task)
        if lst_of_task:
            for i in lst_of_task:
                speak(i)
        print("Task Performed")

    elif 'delete' in inp_task or 'markdone' in inp_task or 'mark done' in inp_task:
        print('Which Task you completed or want to delete')
        print(lst_of_task)
        if lst_of_task:
            for i in lst_of_task:
                speak(i)
        del_task = take_command().lower()
        if del_task in lst_of_task:
            lst_of_task.remove(del_task)
            print("Task Manager Updated")

        else:
            print('Task not in the list')

    else:
        print('Please Choose Appropriate Option')
        speak('Please Choose Appropriate Option')
        taskmanager()





