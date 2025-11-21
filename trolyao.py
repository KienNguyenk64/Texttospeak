import pyttsx3
import speech_recognition
from datetime import date , datetime

robot_ear = speech_recognition.Recognizer()
robot_mounth = pyttsx3.init()
robot_brain = ""

while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)
    print("Robot...")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print(you)

    if you == "":
        robot_brain = "I can't hear you , try again"
    elif "Hello" in you:
        robot_brain = "Hi "
    elif "today" in you :
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "bye" in you:
        print("Robot: " * robot_brain)
        robot_mounth.say(robot_brain)
        robot_mounth.runAndWait()
        break
    else :
        robot_brain = "I am fine thank you and you "
    print(robot_brain)

    print("Robot: " * robot_brain)
    robot_mounth.say(robot_brain)
    robot_mounth.runAndWait()

 