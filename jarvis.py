import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import sys
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Reconnizing...")
        query = recognizer.recognize_google(audio, language= 'en-in')
        print("User said: " + query)
        return query.lower()

    except:
        print("Sorry, I did not catch that, Please try again.")
        return None


def tell_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"the current time is {time}")

def search_wikipedia():
    query = query.replace("wikipedia", "")
    result = wikipedia.summary(query, sentences=1)
    speak(result)

def close_program():
    speak("GoodBye!")
    sys.exit()

def open_chrome():
    speak("Opening Chrome")
    webbrowser.open("https://www.google.com")
def open_youtube():
    speak("Opening Youtube")
    webbrowser.open("https://www.youtube.com/watch?v=Ns3RfaXi0wX")

def main():
    speak("Hello, I am Jarvis, How can I help you?")

    while True:
        query = listen()

        if query is None:
            continue

        if 'time' in query:
            tell_time()
        elif 'wikipedia' in query:
            search_wikipedia(query)

        elif 'quit' in query or 'exit' in query or 'close yourself' in query:
            close_program()

        elif 'open chrome' in query or 'open google':
            open_chrome()

        elif 'open youtube' in query:
            open_youtube()

        else:
            speak("Sorry, I did not understand that.")

if __name__ == "__main__":
    main()

