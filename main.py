import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import pygetwindow as gw
import time
import os
import logging

# Load API key from environment variable
newsapi = os.getenv("NEWS_API_KEY", "207887fc2fa04668b315001b4786eb46")

# Initialize recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set up logging
logging.basicConfig(level=logging.INFO)

def speak(text):
    """Speak the given text using pyttsx3."""
    engine.say(text)
    engine.runAndWait()

def listen_for_audio():
    """Listen for audio and return the recognized text."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        logging.info("Listening for command....")
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
            logging.error(f"An unexpected error occurred: {e}")
            speak("An unexpected error occurred.")
            return None

def close_application(app_name):
    """Close an application by its name."""
    windows = gw.getWindowsWithTitle(app_name)
    if not windows:
        speak(f"Couldn't find any windows with the name '{app_name}'.")
        return
    
    for window in windows:
        logging.info(f"Window found: {window.title}")
        if app_name.lower() in window.title.lower():
            window.close()
            speak(f"Closed {app_name} successfully.")
            return

    speak(f"Couldn't find any windows with the name '{app_name}'.")

def open_website(url, site_name):
    """Open a website in the default browser."""
    speak(f"Opening {site_name}, Sir.")
    webbrowser.open(url)

def fetch_news(category="general"):
    """Fetch the latest news using the News API, allowing for category-specific news."""
    speak("Please wait, fetching the latest news for you.")
    try:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
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
        logging.error(f"Error fetching news: {e}")

def continuously_listen():
    """Keep listening for commands without requiring wake words repeatedly."""
    while True:
        command = listen_for_audio()
        if command:
            logging.info(f"Command received: '{command}'")
            if not process_command(command):
                break
        else:
            time.sleep(1)

def process_command(command):
    """Process the given command."""
    if "open google" in command:
        open_website("http://www.google.com", "Google")
    elif "open facebook" in command:
        open_website("http://www.facebook.com", "Facebook")
    elif "open youtube" in command:
        open_website("http://www.youtube.com", "YouTube")
    elif "open linkedin" in command:
        open_website("http://www.linkedin.com", "LinkedIn")
    elif "play coldplay" in command:
        open_website("https://youtu.be/YykjpeuMNEk?si=8tHA-JkFLoslF2Wv", "Coldplay")
    elif "play on my way" in command:
        open_website("https://youtu.be/dhYOPzcsbGM?si=PBZ7YEBClOyfoPLF", "On My Way")
    elif "news" in command:
        speak("Which category of news would you like? For example: sports, technology, business.")
        category = listen_for_audio() or "general"
        fetch_news(category)
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
        return False
    else:
        speak(f"I didn't recognize the command '{command}'. Please try again.")
        logging.warning(f"Unrecognized command: '{command}'")
    return True

if __name__ == "__main__":
    speak("Hello Respectable Sir, welcome! I am Jarvis.")
    wake_words = ["hello jarvis", "hi jarvis", "jarvis", "hey jarvis", "hello", "hi", "hey"]
    
    # Main loop to listen for wake words
    while True:
        logging.info("Listening for wake word....")  
        command = listen_for_audio()
        
        if command and any(wake_word in command for wake_word in wake_words):
            speak("Yes sir, I'm Jarvis. How can I help you today?")
            continuously_listen()
            break
        elif command:
            logging.warning(f"Unrecognized wake word: '{command}'")
            speak(f"I didn't recognize the wake word '{command}'. Please try again.")
