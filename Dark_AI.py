"""
DARK AI - Voice Assistant
"""

import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import keyboard
import random
import webbrowser
import json
from plyer import notification
from pygame import mixer
import speedtest
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

##############################           Password           ##############################

def verify_password():
    """
    Verify user password with proper validation
    FIXED: Added better error handling and validation
    """
    max_attempts = 3
    
    for attempt in range(max_attempts):
        try:
            password_input = input("Enter Password to open Dark AI: ").strip()
            
            # Read password from file
            if not os.path.exists("password.txt"):
                print("Warning: password.txt not found. Creating default password...")
                with open("password.txt", "w") as f:
                    f.write("Dark AI")
            
            with open("password.txt", "r") as pw_file:
                stored_password = pw_file.read().strip()
            
            if password_input == stored_password:
                print("Welcome Sir! Please speak [Wake Up] to load me up")
                return True
            
            elif attempt == max_attempts - 1:
                print("Maximum attempts reached. Exiting...")
                return False
            
            else:
                print(f"Incorrect password. {max_attempts - attempt - 1} attempts remaining.")
        
        except FileNotFoundError:
            print("Error: password.txt not found")
            return False
        except Exception as e:
            print(f"Error verifying password: {e}")
            return False
    
    return False

##############################          Personal GIF          ##############################

def show_intro():
    """
    Show intro GIF with error handling
    """
    try:
        from intro import play_gif
        play_gif()
    except ImportError:
        print("Warning: intro.py not found, skipping intro animation")
    except Exception as e:
        print(f"Error showing intro: {e}")

##############################           Engine           ##############################

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    """
    Text to speech with error handling
    """
    try:
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        print(f"Error speaking: {e}")

def takeCommand():
    """
    Take voice command from user with improved error handling
    """
    r = speech_recognition.Recognizer()
    
    try:
        with speech_recognition.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.energy_threshold = 300
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, 0, 4)

        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
        return query
    
    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
        return "None"
    except speech_recognition.RequestError as e:
        print(f"Could not request results; {e}")
        return "None"
    except Exception as e:
        print(f"Error: {e}")
        return "None"

##############################           Alarm           ##############################

def alarm(query):
    """
    Set an alarm with improved validation
    """
    try:
        with open("Alarmtext.txt", "a") as timehere:
            timehere.write(query)
        
        if os.path.exists("Alarm.py"):
            os.startfile("Alarm.py")
        else:
            speak("Alarm module not found")
    except Exception as e:
        speak("Could not set alarm")
        print(f"Alarm error: {e}")

##############################           Main Program           ##############################

def main():
    """
    Main program loop with comprehensive error handling
    """
    # Verify password
    if not verify_password():
        sys.exit(1)
    
    # Show intro
    show_intro()
    
    # Main loop
    while True:
        try:
            query = takeCommand().lower()
            
            if "wake up" in query:
                from GreetMe import greetMe
                greetMe()

                while True:
                    try:
                        query = takeCommand().lower()
                        
                        if "go to sleep" in query:
                            speak("Okay Sir, You can call me anytime")
                            break

                        ##############################   Change Password   ##############################

                        elif "change password" in query:
                            speak("What's the new password?")
                            new_pw = input("Enter the new password: ").strip()
                            
                            if new_pw:
                                with open("password.txt", "w") as new_password:
                                    new_password.write(new_pw)
                                speak(f"Done Sir. Your new password is {new_pw}")
                            else:
                                speak("Password cannot be empty")

                        ##############################   Conversations   ##############################

                        elif "hello" in query:
                            speak("Hello Sir, How are you?")

                        elif "i am fine" in query:
                            speak("That's great, sir")

                        elif "how are you" in query:
                            speak("Perfect, sir")

                        elif "thank you" in query:
                            speak("My pleasure, sir")

                        ##############################   Schedule   ##############################

                        elif "schedule my day" in query or "schedule" in query:
                            tasks = []
                            speak("Do you want to clear old tasks? Please speak Yes or No")
                            query = takeCommand().lower()
                            
                            if "yes" in query:
                                with open("tasks.txt", "w") as file:
                                    file.write("")
                            
                            try:
                                no_tasks = int(input("Enter the number of tasks: "))
                                for i in range(no_tasks):
                                    task = input(f"Enter task {i+1}: ").strip()
                                    if task:
                                        tasks.append(task)
                                        with open("tasks.txt", "a") as file:
                                            file.write(f"{i+1}. {task}\n")
                                speak("Tasks added successfully")
                            except ValueError:
                                speak("Invalid number")
                            except Exception as e:
                                speak("Could not add tasks")
                                print(f"Error: {e}")

                        elif "show my schedule" in query:
                            try:
                                with open("tasks.txt", "r") as file:
                                    content = file.read()
                                
                                if content.strip():
                                    mixer.init()
                                    if os.path.exists("notification.mp3"):
                                        mixer.music.load("notification.mp3")
                                        mixer.music.play()
                                    
                                    notification.notify(
                                        title="My Schedule",
                                        message=content,
                                        timeout=15
                                    )
                                else:
                                    speak("No tasks scheduled")
                            except FileNotFoundError:
                                speak("No schedule found")
                            except Exception as e:
                                speak("Could not show schedule")
                                print(f"Error: {e}")

                        ##############################   Open App   ##############################

                        elif "open" in query and "website" not in query:
                            query = query.replace("open", "")
                            query = query.replace("dark", "")
                            query = query.strip()
                            
                            if query:
                                pyautogui.press("super")
                                pyautogui.typewrite(query)
                                pyautogui.sleep(1)
                                pyautogui.press("enter")
                            else:
                                speak("What should I open?")

                        ##############################   Tired (Music)   ##############################

                        elif "tired" in query or "play music" in query:
                            speak("Playing your favourite songs, sir")
                            songs = [
                                "https://youtu.be/xRb8hxwN5zc?si=_y5hVwzIs6ioY-48",
                                "https://www.youtube.com/live/IVjl5u4s-mQ?si=sSpqXLiStaZtdh80",
                                "https://youtu.be/1BKbzZhvUAI?si=SFG7loYeswGx0Td9",
                                "https://youtu.be/r_3zVIyblLQ?si=TMEhr0XAZZzBl-Ms"
                            ]
                            webbrowser.open(random.choice(songs))

                        ##############################   YouTube Controls   ##############################

                        elif "pause" in query:
                            pyautogui.press("k")
                            speak("Video paused")

                        elif "play" in query:
                            pyautogui.press("k")
                            speak("Video resumed")

                        elif "mute" in query:
                            pyautogui.press("m")
                            speak("Video muted")

                        elif "volume up" in query:
                            from keyboard import volumeup
                            speak("Turning volume up, sir")
                            volumeup()

                        elif "volume down" in query:
                            from keyboard import volumedown
                            speak("Turning volume down, sir")
                            volumedown()

                        ##############################   App Control   ##############################

                        elif "close" in query:
                            from Dictapp import closeappweb
                            closeappweb(query)

                        ##############################   Internet Speed   ##############################

                        elif "internet speed" in query:
                            try:
                                speak("Checking internet speed, please wait")
                                wifi = speedtest.Speedtest()
                                upload_net = round(wifi.upload() / 1048576, 2)
                                download_net = round(wifi.download() / 1048576, 2)
                                print(f"Upload: {upload_net} Mbps")
                                print(f"Download: {download_net} Mbps")
                                speak(f"Wifi download speed is {download_net} megabits per second")
                                speak(f"Wifi upload speed is {upload_net} megabits per second")
                            except Exception as e:
                                speak("Could not check internet speed")
                                print(f"Error: {e}")

                        ##############################   Search   ##############################

                        elif "google" in query:
                            from SearchNow import searchGoogle
                            searchGoogle(query)

                        elif "youtube" in query:
                            from SearchNow import searchYoutube
                            searchYoutube(query)

                        elif "wikipedia" in query:
                            from SearchNow import searchWikipedia
                            searchWikipedia(query)

                        ##############################   News   ##############################

                        elif "news" in query:
                            from NewsRead import latestnews
                            latestnews()

                        ##############################   Calculator   ##############################

                        elif "calculate" in query:
                            from Calculatenumbers import Calc
                            query = query.replace("calculate", "")
                            query = query.replace("dark", "")
                            Calc(query)

                        ##############################   WhatsApp   ##############################

                        elif "whatsapp" in query:
                            from Whatsapp import sendMessage
                            sendMessage()

                        ##############################   Temperature   ##############################

                        elif "temperature" in query or "weather" in query:
                            try:
                                from Calculatenumbers import WolfRamAlpha
                                location = os.environ.get('WEATHER_LOCATION', 'Varanasi')
                                weather_query = f"weather in {location}"
                                result = WolfRamAlpha(weather_query)
                                if result:
                                    speak(f"Sir, the weather in {location} is {result}")
                                else:
                                    speak("I couldn't get the weather from Wolfram Alpha. Let me try Google.")
                                    search = f"weather in {location}"
                                    url = f"https://www.google.com/search?q={search}"
                                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
                                    r = requests.get(url, headers=headers, timeout=10)
                                    data = BeautifulSoup(r.text, "html.parser")
                                    temp = data.find("span", id="wob_tm")
                                    if temp:
                                        print(f"Temperature: {temp.text}°C")
                                        speak(f"The current temperature in {location} is {temp.text} degrees Celsius")
                                    else:
                                        speak("I'm sorry, I'm having trouble fetching the weather right now.")
                            except Exception as e:
                                speak("Could not fetch weather info")
                                print(f"Weather error: {e}")

                        ##############################   Set Alarm   ##############################

                        elif "set an alarm" in query:
                            print("Input time example: 10 and 10 and 10")
                            speak("Set the time")
                            a = input("Please tell the time (HH and MM and SS): ").strip()
                            if a:
                                alarm(a)
                                speak("Done, sir")
                            else:
                                speak("No time provided")

                        ##############################   Time   ##############################

                        elif "the time" in query:
                            strTime = datetime.datetime.now().strftime("%H:%M")
                            speak(f"Sir, the time is {strTime}")

                        ##############################   Remember   ##############################

                        elif "remember that" in query:
                            rememberMessage = query.replace("remember that", "")
                            rememberMessage = rememberMessage.replace("dark", "")
                            rememberMessage = rememberMessage.strip()
                            
                            if rememberMessage:
                                speak("You told me to " + rememberMessage)
                                with open("Remember.txt", "w") as remember:
                                    remember.write(rememberMessage)
                            else:
                                speak("What should I remember?")

                        elif "what do you remember" in query:
                            try:
                                with open("Remember.txt", "r") as remember:
                                    content = remember.read()
                                    if content.strip():
                                        speak("You told me to " + content)
                                    else:
                                        speak("I don't remember anything")
                            except FileNotFoundError:
                                speak("I don't remember anything")

                        ##############################   Exit   ##############################

                        elif "finally sleep" in query:
                            speak("Going to sleep, sir")
                            sys.exit(0)

                        ##############################   Shutdown   ##############################

                        elif "shut down the system" in query:
                            speak("Are you sure you want to shutdown the system?")
                            shutdown = input("Do you wish to shutdown your computer? (yes/no): ").strip().lower()
                            if shutdown == "yes":
                                os.system("shutdown /s /t 1")
                            elif shutdown == "no":
                                speak("Shutdown cancelled")
                            else:
                                speak("Invalid response")
                        
                        ##############################   Unknown Command   ##############################
                        
                        elif query != "none":
                            try:
                                from Chatbot import chatbot_response
                                response = chatbot_response(query)
                                speak(response)
                            except Exception:
                                speak("I didn't understand that command. Please try again.")
                    
                    except KeyboardInterrupt:
                        print("\nInterrupted")
                        speak("Goodbye, sir")
                        sys.exit(0)
                    except Exception as e:
                        print(f"Error processing command: {e}")
                        speak("An error occurred. Please try again.")
        
        except KeyboardInterrupt:
            print("\nProgram interrupted")
            sys.exit(0)
        except Exception as e:
            print(f"Fatal error: {e}")
            speak("A critical error occurred")
            sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)
