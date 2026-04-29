import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)

def call_model(messages, model):
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content