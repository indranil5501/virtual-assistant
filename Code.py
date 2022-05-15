import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser 
import os
import smtplib
import wolframalpha


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir")

    elif hour>=12 and hour<18:
        speak("Good afternoon sir")

    else:
        speak("Good evening sir")

    speak("I am jarves sir. I am your virtual assistant. Please tell me how can i help you ")

def takeCommand():
    #microphone input

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        #speak add

        print("say that again please...")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ind5501@gamil.com','2password')
    server.sendmail('ind
5501@gmail.com', to, content)
    server.close()

#api 
def WolfRam(query):
    api_key = "3ATKRH-4VWL344V8R"
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)
    

    try:
        Answer = next(requested.results).text
        return Answer
    except:
        speak("sorry sir not able to process")

    
#calc
def Calculator(query):
    term = str(query)
    term = term.replace("jarvis","")
    term = term.replace("multiply","*")
    trem = term.replace("plus","+")
    trem = term.replace("minus","-")
    trem = term.replace("divide","/")

    Final = str(term)

    try:
        result = WolfRam(Final)
        speak(f"{result}")
    except:
        speak("sorry sir not able to process")

    


if name=="main":
    wishMe()

    

    
    while True:
        query = takeCommand().lower()
        #logic tasks
        if 'wikipedia' in query: #wikipedia
            speak('searching wikipedia..')
            quary = query.replace("wikipedia","")
            result = wikipedia.summary(quary,sentences=2)
            speak("Accroding to wikipedia")
            #print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            speak("ok sir")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'play song' in query: # songs
            music_dir ='F://PROJECT//song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" sir the time is {strTime}")
            
        elif 'open code' in query:
            codePath = "C:\\Users\\indra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to ' in query:
            try:
                speak("what should i say ?")
                content = takeCommand()
                to = "abcd1234@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("sorry sir. i am not adle to send this email")

        elif 'what is the temperature' in query:
            temp=WolfRam('temperature in kolkata')
            speak(f"sir the temperature is {temp}")

        elif 'open calculator' in query:
            speak('what do you want to do sir?')
            quary= takeCommand()
            cal=Calculator(quary)
            speak("sir the result is {cal}")
