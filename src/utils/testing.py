import json
import os
from groq import Groq
from dotenv import load_dotenv

#
load_dotenv()  
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print(client)

system_prompt = """
You are an AI assistant who is expert in breaking down complex problems and then resolve the user query.

For the given user input, analyse the input and break down the problem step by step.
Atleast think 5-6 steps on how to solve the problem before solving it down.

The steps are you get a user input, you analyse, you think, you again think for several times and then return an output with explanation and then finally you validate the output as well before giving final result.

Follow the steps in sequence that is "analyse", "think", "output", "validate" and finally "result".

Rules:
1. Follow the strict JSON output as per Output schema.
2. Always perform one step at a time and wait for next input
3. Carefully analyse the user query

Output Format:
{{ step: "string", content: "string" }}

Example:
Input: What is 2 + 2.
Output: {{ step: "analyse", content: "Alright! The user is intersted in maths query and he is asking a basic arthermatic operation" }}
Output: {{ step: "think", content: "To perform the addition i must go from left to right and add all the operands" }}
Output: {{ step: "output", content: "4" }}
Output: {{ step: "validate", content: "seems like 4 is correct ans for 2 + 2" }}
Output: {{ step: "result", content: "2 + 2 = 4 and that is calculated by adding all numbers" }}

"""

message=[
{
            "role": "system",
            "content": system_prompt,
        }, 
        {
            "role":"user",
            "content":"What is 3 + 4 * 8 / 2 ?"
        }
        ,
        {
            "role":"assistant",
             "content":json.dumps({
            "step": "analyse",
            "content": "The user is asking a mathematical expression involving addition, multiplication, and division. The expression contains multiple operators with different precedences, which need to be evaluated in the correct order."
            })
        }, 
        {
            "role":"assistant",
             "content":json.dumps({
                 
                "step": "think",
                "content": "To evaluate the expression 3 + 4 * 8 / 2, I need to follow the order of operations (PEMDAS/BODMAS), which dictates that I should perform calculations in the following order: Parentheses, Exponents, Multiplication and Division (from left to right), and Addition and Subtraction (from left to right). This means I should first perform the multiplication and then the division before finally adding the result to 3."
                })
        }, 
        {
            "role":"assistant",
                "content":json.dumps({
                "step": "think",
                "content": "Breaking it down further, I should calculate the multiplication 4 * 8 first, which equals 32, and then perform the division 32 / 2, which equals 16. After that, I can add 3 to the result to get the final answer."
                })
        }, 
        {
            "role":"assistant",
            "content":json.dumps({
            "step": "think",
            "content": """Another approach is to think about the expression in terms of the operator precedence. Multiplication and division have higher precedence than addition, so 
            they should be performed first. Also, since multiplication and division have the same precedence, they should be performed from left to right."""
            })
        }, 
        {
            "role":"assistant",
            "content":json.dumps({
            "step": "think",
            "content": "Let's perform the multiplication first: 4 * 8 = 32. Now the expression becomes 3 + 32 / 2. Then perform the division: 32 / 2 = 16. Now the expression becomes 3 + 16."
            })
        }, 
        {
            "role":"assistant",
            "content":json.dumps({
           "step": "output",
            "content": "19"
             })
        }, 
  

]
def main():
    
    chat_completion = client.chat.completions.create(
    response_format={"type": "json_object"},
    messages=message,
    model="llama-3.3-70b-versatile",
    
)
    print(chat_completion.choices[0].message.content)

main()




