import wikipedia #Wikipedia Library
import pyttsx3 #Text-To-Speech Library
import datetime #date and time module
import speech_recognition as sr #Speech Recognition module
import webbrowser #Module to work with web browser
import os #OS Module provides function to interact with operating system
import random #random module to generate pseudo-random variables
import time

engine = pyttsx3.init() # init function to get an engine instance for the speech synthesis
voices = engine.getProperty('voices') #getting details of voices
#print(voices)
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',185) # Changing voice rate
engine.setProperty('volume',1) #Changing volume of assistant

def talk(audio):
    engine.say(audio)
    engine.runAndWait() #Blocks while processing all currently queued commands

def greet():
    h = int(datetime.datetime.now().hour) #h(hour) function will return current time and typecast it in integers
    #print(h)
    if h>=3 and h<12:
        talk("Good morning!")
    
    elif h >= 12 and h < 18:
        talk("Good Afternoon!")
    
    else:
        talk("Good Evening!")

    talk("How may i help you?")

def command():
    #this function takes the mic input and returns a string output
    c = sr.Recognizer()
    with sr.Microphone() as source: # use the default microphone as the audio source
        print("Listening!!!")
        c.pause_threshold = 0.6
        audio = c.listen(source) # listen for the first phrase and extract it into audio data
    try:
        print("Understanding..")
        O = c.recognize_google(audio,language='en-in') #Speech Recognition using Google Speech API
        print(f"Your Command was: {O}\n")
    
    except Exception as err:
        #print(err)
        print("pardon please!")
        return "None"
    return O

def actions(request):
    if "WHO ARE YOU" in request:
        talk("I am your desktop assistant created by Dheeraj Sharma. i can do several tasks such as playing music,opening youtube and search web browser")
        
    elif "YOUR NAME" in request:
        talk("My Name is Pixi")
        
    elif "THANK YOU" in request or "THANKS" in request:
        talk("Your welcome. happy to help you any time")
    
    elif "OPEN WIKIPEDIA" in request:
        url="https://www.wikipedia.com"
        webbrowser.open(url)
        time.sleep(5)

    elif "WIKIPEDIA" in request:
        talk("Searching Wikipedia...")
        request=request.replace("WIKIPEDIA","")
        result = wikipedia.summary(request, sentences = 2 )#The article for which the summary needs to be extracted is passed as a parameter to this method. it'll extract only 2 sentences from summary
        print(result)
        talk(result)
        
    elif "YOUTUBE" in request and "SEARCH" in request:
        request=request.replace("OPEN","")
        request=request.replace("YOUTUBE","")
        request=request.replace("SEARCH","")
        request=request.replace("AND","")
        request=request.replace("ON","")
        talk("Searching...")
        url = "https://www.youtube.com/results?search_query={}".format(request)
        webbrowser.open(url)
        time.sleep(5)

    elif "OPEN YOUTUBE" in request:
        talk("Ok")
        webbrowser.open("www.youtube.com")
        time.sleep(5)
        
    elif "SEARCH" in request:
        request=request.replace("SEARCH","")
        talk("Searching...")
        url = "https://www.google.com.tr/search?q={}".format(request)
        webbrowser.open(url)
        time.sleep(5)

    elif "PLAY MUSIC" in request or "PLAY SONG" in request:
        dir = 'F:\\Song'
        songs=os.listdir(dir)
        print(songs)
        os.startfile(os.path.join(dir,songs[random.randint(0,42)]))
    
    elif "NOTEPAD" in request:
        os.system('notepad')
    
    elif "PAINT" in request:
        os.system('mspaint')
        
    elif 'TIME' in request:
        CurrentTime = datetime.datetime.now().strftime("%H:%M:%S")
        talk(f"the time is {CurrentTime}")
             
    elif "DATE" in request:
        talk(datetime.datetime.now().strftime("%d:%B:%Y"))
        
    elif 'DAY' in request:
        talk(datetime.datetime.now().strftime("%A"))

    elif "QUIT" in request or "EXIT" in request or "BYE" in request:
        talk("Good bye")
        exit()
    else:
        talk("Try Again please")
           
if __name__=="__main__":
    talk("Hello")
    greet()
    while 1:
        request=command().upper()
        actions(request)
         