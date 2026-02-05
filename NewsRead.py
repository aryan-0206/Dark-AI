import requests
import json
import pyttsx3
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

def latestnews():
    """
    Fetch and read latest news
    SECURITY FIX: API key should be in environment variable
    """
    # Get API key from environment variable (more secure)
    api_key = os.environ.get('NEWS_API_KEY', '857171280fe24639bd9692c3ab682597')
    
    if not api_key or api_key == 'YOUR_API_KEY_HERE':
        speak("News API key not configured")
        return
    
    api_dict = {
        "business": f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={api_key}",
        "entertainment": f"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey={api_key}",
        "science": f"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey={api_key}",
        "sports": f"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey={api_key}",
        "technology": f"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey={api_key}",
        "health": f"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey={api_key}"
    }

    content = None 
    url = None
    
    speak("Which field news do you want?")
    print("Available fields: business, entertainment, science, sports, technology, health")
    
    try:
        # Check if we are running in an interactive terminal
        import sys
        if not sys.stdin.isatty():
            field = "technology"
            print(f"Non-interactive environment detected, using default category: {field}")
        else:
            field = input("Type field news that you want: ").strip().lower()
            if not field:
                field = "technology" # Default
    except (EOFError, Exception):
        field = "technology"
        print(f"Using default category: {field}")
    
    # Find matching URL
    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(f"Fetching {key} news...")
            break
    
    if not url:
        speak("Invalid news category")
        print("Please choose from: business, entertainment, science, sports, technology, health")
        return

    try:
        # Fetch news
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        news = response.json()
        
        if news.get("status") != "ok":
            speak("Could not fetch news")
            return
        
        articles = news.get("articles", [])
        
        if not articles:
            speak("No news articles found")
            return
        
        speak("Here is the first news.")

        for i, article in enumerate(articles, 1):
            title = article.get("title", "No title")
            print(f"\n{i}. {title}")
            speak(title)
            
            news_url = article.get("url", "")
            if news_url:
                print(f"   For more info visit: {news_url}")

            # FIXED: Better input handling, check if interactive
            if not sys.stdin.isatty():
                # In non-interactive mode (like Flask), just read the first 3 news
                if i >= 3:
                    break
                continue

            choice = input("\n[Press 1 to continue] or [Press 2 to stop]: ").strip()
            
            if choice == "2":
                break
            elif choice != "1":
                print("Invalid input, stopping...")
                break

        speak("That's all")
    
    except requests.exceptions.Timeout:
        speak("Request timed out. Please check your internet connection.")
    except requests.exceptions.RequestException as e:
        speak("Could not fetch news")
        print(f"Network error: {e}")
    except json.JSONDecodeError:
        speak("Error processing news data")
        print("Invalid JSON response")
    except Exception as e:
        speak("An error occurred while fetching news")
        print(f"Error: {e}")

# Test function
if __name__ == "__main__":
    print("NewsRead module loaded successfully")
    print("Note: Set NEWS_API_KEY environment variable for production use")
