import streamlit as st
from utils.gemini_helper import summarize_notes, generate_quiz

st.set_page_config(page_title="AI Study Buddy", page_icon="📚", layout="centered")

st.title("📚 AI Study Buddy")
st.caption("Paste your class notes → get a summary + auto-generated quiz")

notes = st.text_area("Paste your notes here", height=250, placeholder="Paste your lecture notes, textbook chapter, or any study material...")

col1, col2 = st.columns(2)
with col1:
    num_questions = st.slider("Number of quiz questions", 3, 10, 5)
with col2:
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])

if st.button("Generate Summary & Quiz", type="primary"):
    if not notes.strip():
        st.warning("Please paste some notes first.")
    else:
        with st.spinner("Summarizing your notes..."):
            summary = summarize_notes(notes)
        st.subheader("📝 Summary")
        st.write(summary)

        with st.spinner("Generating quiz questions..."):
            quiz = generate_quiz(notes, num_questions, difficulty)
        st.subheader("🧠 Quiz")
        st.markdown(quiz)

st.divider()
st.caption("Built with Streamlit + Google Gemini API")
