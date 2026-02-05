
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
print(f"API Key found: {'Yes' if api_key else 'No'}")

genai.configure(api_key=api_key)

try:
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Say hello in one word.")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
