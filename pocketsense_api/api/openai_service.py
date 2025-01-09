import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(prompt: str):
    """
    Interacts with OpenAI's GPT models to get a response for a given prompt.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can choose different engines (e.g., GPT-4 if available)
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        return f"OpenAI Error: {str(e)}"
