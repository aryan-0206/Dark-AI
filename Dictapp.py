import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = None
def get_engine():
    global engine
    if engine is None:
        try:
            import pyttsx3
            engine = pyttsx3.init("sapi5")
            voices = engine.getProperty("voices")
            engine.setProperty("voice", voices[0].id)
            engine.setProperty("rate", 170)
        except Exception as e:
            print(f"Error initializing pyttsx3: {e}")
    return engine

def speak(audio):
    try:
        print(f"Assistant: {audio}")
        eng = get_engine()
        if eng:
            eng.say(audio)
            eng.runAndWait()
    except Exception as e:
        print(f"Error speaking: {e}")

# Dictionary of applications
dictapp = {
    "commandprompt": "cmd",
    "paint": "paint",
    "word": "winword",
    "excel": "excel",
    "chrome": "chrome",
    "vscode": "code",
    "powerpoint": "powerpnt",
    "notepad": "notepad",
    "calculator": "calc"
}

def openappweb(query):
    """
    Open applications or websites
    """
    speak("Launching, sir")
    
    # Check if it's a website
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("dark", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        
        try:
            webbrowser.open(f"https://www.{query}")
            return True
        except Exception as e:
            speak(f"Could not open website: {e}")
            return False
    
    # Otherwise, try to open an application
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query.lower():
                try:
                    # FIXED: Added space after 'start'
                    os.system(f"start {dictapp[app]}")
                    return True
                except Exception as e:
                    speak(f"Could not open {app}: {e}")
                    return False
        
        speak("Application not found")
        return False

def closeappweb(query):
    """
    Close browser tabs or applications
    """
    speak("Closing, Sir")
    
    # Handle closing multiple tabs
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("Tab closed")
    
    elif "2 tab" in query or "two tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("2 tabs closed")

    elif "3 tab" in query or "three tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("3 tabs closed")

    elif "4 tab" in query or "four tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("4 tabs closed")

    elif "5 tab" in query or "five tab" in query:
        for _ in range(5):
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
        speak("5 tabs closed")
    
    # Close application by name
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query.lower():
                try:
                    # FIXED: Added space after 'im' and proper formatting
                    os.system(f"taskkill /f /im {dictapp[app]}.exe")
                    speak(f"{app} closed")
                    return True
                except Exception as e:
                    speak(f"Could not close {app}: {e}")
                    return False
        
        speak("Application not found")
        return False

# Test function
if __name__ == "__main__":
    print("Dictapp module loaded successfully")
    print("Available applications:")
    for key in dictapp.keys():
        print(f"  - {key}")
