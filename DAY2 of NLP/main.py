# main.py

import streamlit as st
import nltk

from matcher import match_keywords
from keywords import get_all_keywords
from sample_resume import SAMPLE_RESUME
from utils import read_uploaded_file, clean_multiline_input


# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')


# Streamlit UI setup
st.set_page_config(page_title="Resume Keyword Matcher", layout="centered")
st.title("📄 Resume Keyword Matcher")
st.markdown("Match your resume with job keywords using NLP")


# Resume input
uploaded_resume = st.file_uploader("Upload Resume (.txt)", type=["txt"])

if uploaded_resume is not None:
    resume_text = read_uploaded_file(uploaded_resume)
else:
    resume_text = SAMPLE_RESUME


# Keyword input
st.markdown("### 🧠 Job Description Keywords")
keywords_input = st.text_area(
    "Paste job skills or keywords here (one per line)", height=200
)

if keywords_input.strip():
    keywords_list = clean_multiline_input(keywords_input)
else:
    keywords_list = get_all_keywords()


# Button to match
if st.button("🔍 Match Resume"):
    if not resume_text or not keywords_list:
        st.warning("Please upload a resume and enter keywords.")
    else:
        result = match_keywords(resume_text, keywords_list)

        st.success(f"✅ Match Score: {result['score']}%")

        st.markdown("### ✅ Matched Keywords")
        st.write(result["matched"])

        st.markdown("### ❌ Missing Keywords")
        st.write(result["unmatched"])
