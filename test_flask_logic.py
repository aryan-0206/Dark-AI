
from flask_app import process_command, speak

# Test basic greeting
print("Testing 'hello'...")
res = process_command("hello")
print(f"Result: '{res}'")

# Test fallback to chatbot
print("\nTesting 'who are you'...")
res = process_command("who are you")
print(f"Result: '{res}'")
