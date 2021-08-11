import pyttsx3

engine = pyttsx3.init()
while True:
    ans = input('enter your text.... :')
    engine.say(ans)
    engine.runAndWait()
    