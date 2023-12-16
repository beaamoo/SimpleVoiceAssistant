import speech_recognition as sr
import pyaudio
import pywhatkit
from gtts import gTTS
from playsound import playsound

def speech(text):
    print(text)
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)
    output.save("./sounds/output.mp3")
    playsound("./sounds/output.mp3")

def get_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        playsound("./sounds/activate.wav")
        audio = r.listen(source)
        try:
            said = r.recognize_google(audio)
            print(f"You said: {said}")
            return said
        except:
            print("Sorry, I did not get that")
            return ""

text = get_speech()

if "youtube" in text.lower():
    video = text.replace("youtube", "")
    speech("Playing " + video + " on YouTube")
    pywhatkit.playonyt(video)
elif "google" in text.lower():
    search = text.replace("google", "")
    speech("Searching for " + search)
    pywhatkit.search(search)
else:
    speech("Please say the command again.")