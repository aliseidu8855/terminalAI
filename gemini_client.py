
import os
import google.generativeai as genai
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

# Configure the Gemini client
genai.configure(api_key=api_key)

# We use gemini-1.5-flash, which is fast and has a generous free tier.
model = genai.GenerativeModel('gemini-1.5-flash-latest')

async def generate_response(prompt: str) -> str:
    """
    Generates a response from the Gemini API.
    """
    try:
        # The API call method for Gemini
        response = await model.generate_content_async(prompt)
        
        # Gemini's response structure is simpler for text
        return response.text.strip()
    except Exception as e:
        # Catching a broad exception is okay here, but log the specific error.
        print(f"Gemini API error: {e}")
        raise HTTPException(status_code=503, detail="Error communicating with Gemini API.")