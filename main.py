import pyttsx3
text_speech = pyttsx3.init()
text_speech.say("welcome , Speaker turn on")

while True:
    
    answer = input("enter your text that you want to speech")
    if answer =="q":
        text_speech.say("Speaker turn off thank you")
        text_speech.runAndWait()
        break
    text_speech.say(answer)
    text_speech.runAndWait()
    