import os
from openai import OpenAI

def call_model(messages, model):

    # Route based on model name
    if model.startswith("openrouter/"):
        client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url=os.getenv("OPENROUTER_BASE_URL")
        )

        model_name = model.replace("openrouter/", "")

    else:
        # Default is Groq
        client = OpenAI(
            api_key=os.getenv("API_KEY"),
            base_url=os.getenv("BASE_URL")
        )

        model_name = model

    response = client.chat.completions.create(
        model=model_name,
        messages=messages
    )

    return response.choices[0].message.content