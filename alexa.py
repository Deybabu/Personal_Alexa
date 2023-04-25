import speech_recognition as sr
import pyttsx3
import pywhatkit

listener=sr.Recognizer()

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#engine talk
def engine_talk(text):
    engine.say(text)
    engine.runAndWait()
    
def user_commands():
    try:
        with sr.Microphone() as source:
            engine.say("My name is Alexa")
            engine.say('How Can I help you sir')
            engine.say('Say anything with starting with Alexa')
            engine.runAndWait()
            print("Start speaking")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
    except:
        pass
    return command
def run_alexa():
    command=user_commands()
    if 'play' in command:
        song=command.replace('play','')
        print('New command is'+song)
        engine_talk('Playing'+song)
        pywhatkit.playonyt(song)
    else:
        engine_talk('I could not hear you properly')

run_alexa()

