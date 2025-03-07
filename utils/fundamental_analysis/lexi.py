import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

LEXI_API_KEY = os.getenv('LEXI_API_KEY')
LEXI_URL = os.getenv('LEXI_URL')

client = OpenAI(
    base_url=LEXI_URL,
    api_key=LEXI_API_KEY
)

# response = client.chat.completions.create(
#     model="Lexi", # Available models: Lexi, LexiOnboarding
#     messages=[
#         {"role": "user", "content": "Hello!"}
#     ]
# )

def lexi_chat(message: str):
    try:
        response = client.chat.completions.create(
            model="Lexi",
            messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)