import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Add it to your .env file.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")


def summarize_notes(notes: str) -> str:
    """Summarize study notes into concise bullet points."""
    prompt = f"""Summarize the following study notes into clear, concise bullet points.
Keep the key concepts, definitions, and important facts. Keep it under 200 words.

Notes:
{notes}
"""
    response = model.generate_content(prompt)
    return response.text


def generate_quiz(notes: str, num_questions: int, difficulty: str) -> str:
    """Generate a quiz with answers based on the notes."""
    prompt = f"""Based on the following study notes, create {num_questions} {difficulty.lower()}-level
multiple choice quiz questions. For each question, give 4 options labeled A-D,
mark the correct answer clearly, and add a one-line explanation.

Format each question like this:
**Q1. <question>**
A) option
B) option
C) option
D) option
**Answer:** <letter> — <short explanation>

Notes:
{notes}
"""
    response = model.generate_content(prompt)
    return response.text
