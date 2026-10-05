from dotenv import load_dotenv
import os

from groq import Groq

load_dotenv()

key = os.getenv("GEMINI_API_KEY")

if key:
    print("GROQ_API_KEY is set")
else:
    print("GROQ_API_KEY is not set")

