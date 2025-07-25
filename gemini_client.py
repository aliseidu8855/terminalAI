
import os
import google.generativeai as genai
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash-latest')

async def generate_response(prompt: str) -> str:
    """
    Generates a response from the Gemini API.
    """
    try:
        response = await model.generate_content_async(prompt)
        
        return response.text.strip()
    except Exception as e:
        print(f"Gemini API error: {e}")
        raise HTTPException(status_code=503, detail="Error communicating with Gemini API.")