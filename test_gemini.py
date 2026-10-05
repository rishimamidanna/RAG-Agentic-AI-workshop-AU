from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("GEMINI_API_KEY")

if key:
    print("GEMINI_API_KEY is set")
else:
    print("GEMINI_API_KEY is not set")