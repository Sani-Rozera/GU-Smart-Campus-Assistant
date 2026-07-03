import os
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from google import genai

env_path = find_dotenv()
if not env_path:
    env_path = Path(__file__).resolve().parents[1] / ".env"

load_dotenv(dotenv_path=env_path)


def get_llm():

    api_key = os.getenv("GOOGLE_API_KEY")

    print("API Key:", api_key)

    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in .env file")

    return genai.Client(api_key=api_key)


def get_prompt():
    return """
You are an AI Assistant for Geeta University.

Use ONLY the information provided in the context to answer the user's question.

If the context contains partial information, answer using whatever relevant information is available.

If the answer is completely unavailable in the context, reply:
"Sorry, this information is not available in the provided university documents."

Context:
{context}

Question:
{question}

Answer:
"""
