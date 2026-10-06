from dotenv import load_dotenv
import os
from google import genai

# Load variables from .env
load_dotenv()

# Get Gemini API key
key = os.getenv("GEMINI_API_KEY")

if key:
    print("GEMINI_API_KEY is loaded successfully")
else:
    print("GEMINI_API_KEY is not set")

# Create Gemini client
client = genai.Client(api_key=key)

# Create a chat session (the recommended way)
chat = client.chats.create(model="gemini-3.8-flash")

# Send message to Gemini (the new recommended way)
response = chat.send_message("what is aditya university")

# Print Gemini's response
print(response.text)