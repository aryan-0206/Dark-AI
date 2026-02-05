import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

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
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    
    try:
        print("Understanding....")
        # FIXED: Changed from recognize_google_cloud to recognize_google
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def searchGoogle(query):
    """
    Search on Google
    """
    if "google" in query:
        import wikipedia as googleScrap 
        query = query.replace("dark", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        query = query.strip()  # FIXED: Added strip
        
        if not query:
            speak("What should I search for?")
            return
        
        speak("This is what I found on Google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            speak(result)

        except Exception as e:
            speak("No speakable output available")
            print(f"Google search error: {e}")

def searchYoutube(query):
    """
    Search on YouTube
    """
    if "youtube" in query:
        speak("This is what I found for your search!")
        query = query.replace("dark", "")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        query = query.strip()  # FIXED: Added strip
        
        if not query:
            speak("What should I search for on YouTube?")
            return
        
        try:
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            pywhatkit.playonyt(query)
            speak("Done, sir")
        except Exception as e:
            speak("Could not open YouTube")
            print(f"YouTube search error: {e}")

def searchWikipedia(query):
    """
    Search on Wikipedia
    """
    if "wikipedia" in query:
        speak("Searching from Wikipedia....")
        query = query.replace("wikipedia", "")
        query = query.replace("dark", "")
        query = query.replace("search wikipedia", "")
        query = query.strip()  # FIXED: Added strip
        
        if not query:
            speak("What should I search for on Wikipedia?")
            return
        
        try:
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
            print(results)
            speak(results)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("Multiple results found. Please be more specific.")
            print(f"Disambiguation error: {e}")
        except wikipedia.exceptions.PageError:
            speak("No Wikipedia page found for that query.")
        except Exception as e:
            speak("Could not search Wikipedia")
            print(f"Wikipedia search error: {e}")

# Test function
if __name__ == "__main__":
    print("SearchNow module loaded successfully")
    print("Available functions: searchGoogle, searchYoutube, searchWikipedia")
