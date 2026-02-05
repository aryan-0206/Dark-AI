import wolframalpha
import pyttsx3
import speech_recognition
import os

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

def WolfRamAlpha(query):
    """
    Query WolframAlpha API
    SECURITY FIX: API key should be in environment variable or config file
    """
    # Get API key from environment variable (more secure)
    apikey = os.environ.get('WOLFRAM_API_KEY', 'J4WHVP-HHGQRKE2X6')
    
    if not apikey or apikey == 'YOUR_API_KEY_HERE' or apikey.strip() == "":
        speak("WolframAlpha API key not configured")
        return None
    
    try:
        requester = wolframalpha.Client(apikey)
        requested = requester.query(query)
        answer = next(requested.results).text
        return answer
    except StopIteration:
        speak("The value is not answerable")  # FIXED: typo "vlaue" -> "value"
        return None
    except Exception as e:
        speak(f"Error querying WolframAlpha: {str(e)}")
        return None

def Calc(query):
    """
    Process calculation queries
    """
    Term = str(query)
    Term = Term.replace("dark", "")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("divide", "/")
    Term = Term.replace("times", "*")
    Term = Term.replace("into", "*")

    Final = str(Term).strip()
    
    if not Final:
        speak("No calculation provided")
        return None
    
    try:
        result = WolfRamAlpha(Final)
        if result:
            print(f"Result: {result}")
            speak(result)
            return result
        else:
            speak("The value is not answerable")  # FIXED: typo
            return None
    
    except Exception as e:
        speak("The value is not answerable")
        print(f"Calculation error: {e}")
        return None

# Test function
if __name__ == "__main__":
    print("Calculator module loaded successfully")
    # Test calculation
    test_query = "5 plus 5"
    print(f"Testing: {test_query}")
    result = Calc(test_query)
    if result:
        print(f"Test result: {result}")
