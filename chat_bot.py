from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
from google import genai
client = Groq(
    api_key = os.getenv("GEMINI_API_KEY")
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="gemini-3.7-flash"
)

# Print the completion returned by the LLM.
print(chat_completion.choices[0].message.content)