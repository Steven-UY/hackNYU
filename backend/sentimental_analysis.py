import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from typing import Dict

# Initialize the OpenAI client with the API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_sentiment(text_content: str) -> Dict:
    messages = [
        {"role": "system", "content": "You are a sentiment analysis assistant. Score negativity from 0-10."},
        {"role": "user", "content": f"""Analyze the sentiment of: '{text_content}'
        Return in JSON format:
        {{
            "sentiment": "positive/negative/neutral",
            "score": 0-10 (0 being most positive, 10 being most negative),
            "explanation": "brief explanation",
            "should_blur": "true" if score > 6 else "false"
        }}"""}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=100,
            temperature=0.3,
        )
        
        # Parse JSON response properly
        result = json.loads(response.choices[0].message.content.strip())
        # Convert string boolean to Python boolean
        result['should_blur'] = result['should_blur'].lower() == 'true'
        return result
        
    except Exception as e:
        print(f"Error parsing response: {e}")
        return {
            "sentiment": "neutral",
            "score": 5,
            "explanation": "Error analyzing sentiment",
            "should_blur": False
        }
    
    


