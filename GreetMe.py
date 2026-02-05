import pyttsx3
import datetime

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

def greetMe():
    """
    Greet user based on time of day
    """
    try:
        hour = int(datetime.datetime.now().hour)
        
        if hour >= 0 and hour < 12:
            speak("Good Morning, Sir")
        elif hour >= 12 and hour < 18:
            speak("Good Afternoon, Sir")
        else: 
            speak("Good Evening, Sir")

        speak("Please tell me, how can I help you?")
        
    except Exception as e:
        print(f"Error in greetMe: {e}")
        speak("Hello Sir, how can I help you?")

# Test function
if __name__ == "__main__":
    print("Testing GreetMe module...")
    greetMe()
