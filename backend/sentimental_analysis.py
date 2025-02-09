import os
from openai import OpenAI
from dotenv import load_dotenv

# Initialize the OpenAI client with the API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_sentiment(text_content: str) -> str:
    # Prepare a conversation with a system prompt and the user's sentiment request.
    messages = [
        {"role": "system", "content": "You are a sentiment analysis assistant."},
        {"role": "user", "content": f"Analyze the sentiment of the following text: '{text_content}'. Is it positive, negative, or neutral?"}
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=10,
        temperature=0.5,
    )

    sentiment = response.choices[0].message.content.strip()
    return sentiment

