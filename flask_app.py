import os
import datetime
import random
import webbrowser
import pyautogui
import requests
import json
import threading
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import existing modules
import SearchNow
import NewsRead
import Calculatenumbers
import Dictapp
import GreetMe
import Whatsapp

app = Flask(__name__)
CORS(app)

import Chatbot

# Mocking the speak function to capture output
response_buffer = []

def speak(text):
    print(f"Assistant: {text}")
    if text and text not in response_buffer:
        response_buffer.append(text)

# Monkey-patch speak in all modules to redirect output to the web UI
modules_to_patch = [SearchNow, NewsRead, Calculatenumbers, Dictapp, GreetMe, Whatsapp, Chatbot]
for module in modules_to_patch:
    if hasattr(module, 'speak'):
        module.speak = speak

def process_command(query):
    global response_buffer
    response_buffer = []
    query = query.lower().strip()
    print(f"\nUser Command: {query}")
    
    if not query or query == "none":
        return ""
    
    if "hello" in query:
        speak("Hello Sir, How are you?")
    
    elif "i am fine" in query:
        speak("That's great, sir")
    
    elif "how are you" in query:
        speak("Perfect, sir")
    
    elif "thank you" in query:
        speak("My pleasure, sir")
    
    elif "open" in query and "website" not in query:
        app_name = query.replace("open", "").replace("dark", "").strip()
        if app_name:
            pyautogui.press("super")
            pyautogui.typewrite(app_name)
            pyautogui.sleep(1)
            pyautogui.press("enter")
            speak(f"Opening {app_name}")
        else:
            speak("What should I open?")
            
    elif "google" in query:
        from SearchNow import searchGoogle
        searchGoogle(query)
        speak("Searching Google...")
        
    elif "youtube" in query:
        from SearchNow import searchYoutube
        searchYoutube(query)
        speak("Opening YouTube...")
        
    elif "wikipedia" in query:
        from SearchNow import searchWikipedia
        searchWikipedia(query)
        speak("Searching Wikipedia...")
        
    elif "temperature" in query or "weather" in query:
        try:
            from Calculatenumbers import WolfRamAlpha
            location = os.environ.get('WEATHER_LOCATION', 'Varanasi')
            weather_query = f"weather in {location}"
            result = WolfRamAlpha(weather_query)
            if result:
                speak(f"The current weather in {location} is {result}")
            else:
                speak("I couldn't get the weather from Wolfram Alpha. Let me try Google.")
                # Fallback to Google Search (improved scraping)
                search = f"weather in {location}"
                url = f"https://www.google.com/search?q={search}"
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
                r = requests.get(url, headers=headers, timeout=10)
                data = BeautifulSoup(r.text, "html.parser")
                # Try multiple possible selectors
                temp = data.find("span", id="wob_tm")
                if temp:
                    speak(f"The current temperature in {location} is {temp.text} degrees Celsius")
                else:
                    speak("I'm sorry, I'm having trouble fetching the weather right now.")
        except Exception as e:
            print(f"Weather error: {e}")
            speak("Could not fetch weather information.")

    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir, the time is {strTime}")

    elif "tired" in query or "play music" in query:
        speak("Playing your favourite music, sir")
        songs = [
            "https://youtu.be/xRb8hxwN5zc?si=_y5hVwzIs6ioY-48",
            "https://www.youtube.com/live/IVjl5u4s-mQ?si=sSpqXLiStaZtdh80",
            "https://youtu.be/1BKbzZhvUAI?si=SFG7loYeswGx0Td9"
        ]
        webbrowser.open(random.choice(songs))

    elif "news" in query:
        try:
            from NewsRead import latestnews
            # Note: NewsRead usually speaks directly. 
            # For web, we might need to modify it or just let it speak on server.
            latestnews()
            speak("Reading the latest news...")
        except:
            speak("Could not read news at the moment.")

    elif "calculate" in query:
        try:
            from Calculatenumbers import Calc
            calc_query = query.replace("calculate", "").replace("dark", "").strip()
            Calc(calc_query)
            speak(f"Calculating {calc_query}")
        except:
            speak("Calculation failed.")

    elif "remember that" in query:
        remember_msg = query.replace("remember that", "").replace("dark", "").strip()
        if remember_msg:
            with open("Remember.txt", "w") as f:
                f.write(remember_msg)
            speak(f"I'll remember that you told me to: {remember_msg}")
        else:
            speak("What should I remember?")

    elif "what do you remember" in query:
        try:
            with open("Remember.txt", "r") as f:
                content = f.read()
                if content.strip():
                    speak(f"You told me to remember: {content}")
                else:
                    speak("I don't remember anything yet.")
        except FileNotFoundError:
            speak("I don't remember anything.")

    elif "shutdown" in query:
        speak("I cannot shutdown the system from the web interface for safety reasons.")

    else:
        try:
            from Chatbot import chatbot_response
            response = chatbot_response(query)
            if response and response.strip():
                speak(response)
            else:
                speak("I'm sorry, I'm having trouble thinking of a response right now.")
        except Exception as e:
            print(f"Chatbot bridge error: {e}")
            speak("I encountered an error trying to process your request.")

    return " ".join(response_buffer) if response_buffer else "I heard you, but I don't know how to respond to that."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/command", methods=["POST"])
def command():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        query = data.get("command", "")
        if not query:
            return jsonify({"error": "No command provided"}), 400
        
        response_text = process_command(query)
        return jsonify({"response": response_text})
    except Exception as e:
        print(f"API Error: {e}")
        return jsonify({"error": str(e)}), 500

def open_browser():
    # Use 5000 as standard Flask port
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    # Use a slightly longer timer to ensure server is fully ready
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        print("Launching browser...")
        threading.Timer(1.5, open_browser).start()
    
    # Set debug=False for a smoother experience without reloader overhead
    # Set use_reloader=False to ensure the browser timer only runs once
    app.run(host="127.0.0.1", port=5000, debug=False)
