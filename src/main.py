import json
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()  # take environment variables

# Initialize Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def main():
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Hi how are you ? ",
        }
    ],
    model="llama-3.3-70b-versatile",
)
    print(chat_completion.choices[0].message.content)



main()