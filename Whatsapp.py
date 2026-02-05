import pywhatkit
import pyttsx3
import datetime
import speech_recognition
from datetime import timedelta
import os
import json

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

def takeCommand():
    """
    Take voice command from user
    """
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    
    except Exception as e:
        print("Say that again")
        return "None"
    
    return query

def load_contacts():
    """
    Load contacts from config file
    SECURITY FIX: Phone numbers should be in config, not hardcoded
    """
    config_file = "whatsapp_config.json"
    
    if os.path.exists(config_file):
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading contacts: {e}")
    
    # Default contacts (create config file if it doesn't exist)
    default_contacts = {
        "1": {
            "name": "Person 1",
            "phone": "+910000000000"  # Replace with actual number
        },
        "2": {
            "name": "Person 2",
            "phone": "+910000000000"  # Replace with actual number
        }
    }
    
    # Save default config
    try:
        with open(config_file, 'w') as f:
            json.dump(default_contacts, f, indent=4)
        print(f"Created {config_file}. Please update with your contacts.")
    except Exception as e:
        print(f"Could not create config file: {e}")
    
    return default_contacts

def sendMessage(contact_choice=None, message_content=None):
    """
    Send WhatsApp message
    """
    import sys
    contacts = load_contacts()
    
    try:
        if contact_choice is None:
            if not sys.stdin.isatty():
                speak("WhatsApp messaging requires manual input and is not available in web mode yet.")
                return
            
            speak("Who do you want to message?")
            # Display available contacts
            print("\nAvailable contacts:")
            for key, contact in contacts.items():
                print(f"{key}. {contact['name']}")
            contact_choice = input("\nEnter contact number: ").strip()
        
        if contact_choice not in contacts:
            speak("Invalid contact selection")
            return
        
        contact = contacts[contact_choice]
        phone = contact['phone']
        
        if not phone or phone == "+910000000000":
            speak("Phone number not configured.")
            return
        
        if message_content is None:
            if not sys.stdin.isatty():
                speak("Message content missing.")
                return
            speak(f"What's the message for {contact['name']}?")
            message_content = input("Enter the message: ").strip()
        
        if not message_content:
            speak("No message provided")
            return
        
        # Calculate time (2 minutes from now)
        now = datetime.datetime.now()
        send_time = now + timedelta(minutes=2)
        time_hour = int(send_time.strftime("%H"))
        time_min = int(send_time.strftime("%M"))
        
        speak(f"Sending message to {contact['name']} at {time_hour}:{time_min}")
        print(f"Message will be sent at {time_hour}:{time_min}")
        
        try:
            pywhatkit.sendwhatmsg(phone, message_content, time_hour, time_min)
            speak("Message scheduled successfully")
        except Exception as e:
            speak("Could not send message")
            print(f"WhatsApp error: {e}")
    
    except KeyboardInterrupt:
        print("\nCancelled")
        speak("Cancelled")
    except Exception as e:
        speak("An error occurred")
        print(f"Error: {e}")

# Test function
if __name__ == "__main__":
    print("WhatsApp module loaded successfully")
    print("Note: Update whatsapp_config.json with your contacts")
    
    # Create sample config if it doesn't exist
    load_contacts()
