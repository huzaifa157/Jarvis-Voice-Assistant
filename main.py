import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import pygetwindow as gw
import time

newsapi = "207887fc2fa04668b315001b4786eb46"

# Initialize recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Speak the given text using pyttsx3."""
    engine.say(text)
    engine.runAndWait()

def listen_for_audio():
    """Listen for audio and return the recognized text."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening....")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            return recognizer.recognize_google(audio).strip().lower()
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            speak("There was an error with the speech recognition service.")
            return None   
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            speak("An unexpected error occurred.")
            return None
    
def close_application(app_name):
    """Close an application by its name."""
    windows = gw.getWindowsWithTitle(app_name)
    if not windows:
        speak(f"Couldn't find any windows with the name '{app_name}'.")
        return
    
    for window in windows:
        # Print all window titles to debug
        print(f"Window found: {window.title}")
        
        if app_name.lower() in window.title.lower():
            window.close()
            speak(f"Closed {app_name} successfully.")
            return

    speak(f"Couldn't find any windows with the name '{app_name}'.")

if __name__ == "__main__":
    speak("Hello Respectable Sir, welcome! I am Jarvis.")
    wake_words = ["hello jarvis", "hi jarvis", "jarvis", "hey jarvis", "hello", "hi", "hey"]
    
    while True:
        print("Listening for wake word....")  
        command = listen_for_audio()
        
        if command and any(wake_word in command for wake_word in wake_words):
            speak("Yes sir, I'm Jarvis. How can I help you today?")
            break
        elif command:
            print(f"Unrecognized wake word: '{command}'")
            speak(f"I didn't recognize the wake word '{command}'. Please try again.")
    
    while True:
        print("Listening for command....")
        command = listen_for_audio()
        
        if command:
            print(f"Command received: '{command}'")
            if "open google" in command:
                speak("Opening Google, Sir.")
                webbrowser.open("http://www.google.com")
            elif "open facebook" in command:
                speak("Opening Facebook, Sir.")
                webbrowser.open("http://www.facebook.com")
            elif "open youtube" in command:
                speak("Opening YouTube, Sir.")
                webbrowser.open("http://www.youtube.com")
            elif "open linkedin" in command:
                speak("Opening LinkedIn, Sir.")
                webbrowser.open("http://www.linkedin.com")
            elif "play coldplay" in command:
                speak("Playing Coldplay for you!")
                webbrowser.open("https://youtu.be/YykjpeuMNEk?si=8tHA-JkFLoslF2Wv")
            elif "play on my way" in command:
                speak("Playing 'On My Way' for you!")
                webbrowser.open("https://youtu.be/dhYOPzcsbGM?si=PBZ7YEBClOyfoPLF")
            elif "news" in command:
                speak("Please wait, fetching the latest news for you.")
                try:
                    r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
                    if r.status_code == 200:
                        data = r.json()
                        print("Response Data:", data)
                        articles = data.get('articles', [])
                        if articles:
                            for article in articles[:5]:
                                speak(article['title'])
                        else:
                            speak("I couldn't find any news articles.")
                    else:
                        speak("Failed to fetch the news. Please try again later.")
                except requests.RequestException as e:
                    speak("There was an error fetching the news.")
                    print(f"Error fetching news: {e}")
            elif "close google" in command:
                close_application("Google")
            elif "close facebook" in command:
                close_application("Facebook")
            elif "close youtube" in command:
                close_application("YouTube")
            elif "close linkedin" in command:
                close_application("LinkedIn")
            elif "bye" in command or "exit" in command:
                speak("Goodbye, Sir. Have a great day!")
                break
            else:
                speak(f"I didn't recognize the command '{command}'. Please try again.")
                print(f"Unrecognized command: '{command}'")
        else:
            # Sleep briefly before checking for commands again
            time.sleep(1)
