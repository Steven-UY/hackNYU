import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_sentiment(text_content: str) -> str:

    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = f"Analyze the sentiment of the following text: '{text_content}'. Is it positive, negative, or neutral?",
        max_tokens = 10,
        n = 10,
        stop = None,
        temperature = 0.5
    )

    sentiment = response.choices[0].text.strip()
    return sentiment


