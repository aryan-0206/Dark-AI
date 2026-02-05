
import requests
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def chatbot_response(query):
    """
    Get response from Gemini AI using REST API (more reliable than SDK in some environments)
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key or api_key == "YOUR_API_KEY_HERE":
        return "My AI brain is not configured. Please add your Gemini API key to the .env file."

    # Using gemini-flash-latest as it's more likely to be available
    model = "gemini-flash-latest"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    payload = {
        "contents": [{
            "parts": [{
                "text": f"You are Dark AI, a helpful and friendly AI voice assistant. User says: {query}"
            }]
        }],
        "generationConfig": {
            "temperature": 0.7,
            "topK": 40,
            "topP": 0.95,
            "maxOutputTokens": 1024,
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        
        # If 1.5-flash is not found (404), try gemini-pro
        if response.status_code == 404:
            model = "gemini-pro"
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
            response = requests.post(url, headers=headers, json=payload, timeout=15)

        if response.status_code == 200:
            result = response.json()
            try:
                # Extract text from the response structure
                text = result['candidates'][0]['content']['parts'][0]['text']
                return text.strip()
            except (KeyError, IndexError, TypeError):
                print(f"Unexpected API response structure: {result}")
                return "I'm sorry, I couldn't process the AI response."
        else:
            print(f"API Error {response.status_code}: {response.text}")
            error_msg = response.json().get('error', {}).get('message', 'Unknown error')
            if "quota" in error_msg.lower():
                return "I'm thinking too much right now (API quota reached). Please wait a moment."
            return "I'm having a little trouble connecting to my AI brain."

    except requests.exceptions.Timeout:
        return "I'm sorry, I'm taking too long to think. Please try again."
    except Exception as e:
        print(f"Chatbot Error: {e}")
        return "I'm having a little trouble thinking right now."

def speak(audio):
    """Fallback speak function"""
    print(f"Assistant: {audio}")

if __name__ == "__main__":
    print("Chatbot REST module testing...")
    test_query = "Hello"
    print(f"Query: {test_query}")
    print(f"Response: {chatbot_response(test_query)}")
