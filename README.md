# 📚 AI Study Buddy

An AI-powered web app that turns your class notes into a concise summary and an
auto-generated quiz — built with Streamlit and Google's Gemini API.

## Features
- Paste any study notes (lecture notes, textbook excerpts, etc.)
- Get a clean, bullet-point summary in seconds
- Auto-generate multiple-choice quiz questions with answers and explanations
- Adjustable number of questions and difficulty level

## Tech Stack
- Python
- Streamlit (UI)
- Google Gemini API (generative AI)
- python-dotenv (environment config)

## Project Structure
```
ai-study-buddy/
├── app.py                  # Streamlit app entry point
├── utils/
│   ├── __init__.py
│   └── gemini_helper.py    # Gemini API calls (summarize, quiz generation)
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Setup

1. Clone the repo
   ```bash
   git clone https://github.com/<your-username>/ai-study-buddy.git
   cd ai-study-buddy
   ```

2. Create a virtual environment and install dependencies
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Get a free Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

4. Create a `.env` file (copy `.env.example`) and add your key
   ```
   GEMINI_API_KEY=your_actual_key_here
   ```

5. Run the app
   ```bash
   streamlit run app.py
   ```

## Future Improvements
- Support PDF/DOCX upload instead of pasting text
- Save quiz history per session
- Export quiz as a downloadable PDF
- Add spaced-repetition style flashcards

## License
MIT
