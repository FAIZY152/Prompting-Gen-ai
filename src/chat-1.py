import json
import os
from groq import Groq
from dotenv import load_dotenv

# practice-few-shot prompts


load_dotenv()  # take environment variables

# Initialize Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

system_prompt = """
You are an AI Assistant who is specialized in maths.
You should not answer any query that is not related to maths.

For a given query help user to solve that along with explanation.

Example:
Input: 2 + 2
Output: 2 + 2 is 4 which is calculated by adding 2 with 2.

Input: 3 * 10
Output: 3 * 10 is 30 which is calculated by multipling 3 by 10. Funfact you can even multiply 10 * 3 which gives same result.

Input: Why is sky blue?
Output: Bruh? You alright? Is it maths query?
"""


def main():
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": system_prompt,
        }, 
        {
            "role":"user",
            "content":"What is 12 * 12 ?"
        }
    ],
    model="llama-3.3-70b-versatile",
)
    print(chat_completion.choices[0].message.content)



main()




