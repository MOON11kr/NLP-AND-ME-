# streamlit_nlp_qgen.py

import streamlit as st
import spacy
import random
import fitz  # PyMuPDF
from io import StringIO
from transformers import pipeline


# Load NLP models
nlp = spacy.load("en_core_web_sm")
summarizer = pipeline("summarization")
mcq_gen = pipeline(
    "text2text-generation",
    model="valhalla/t5-small-qg-prepend"
)


# ----------- Streamlit Setup -----------
st.set_page_config(
    page_title="NLP Question Generator",
    layout="centered"
)

st.title("📘 NLP Question Generator")
st.caption("Summarization + MCQ + Fill-in-the-blank")


# ----------- Extract Text -----------

def extract_text(file):
    if file.name.endswith(".txt"):
        stringio = StringIO(file.read().decode("utf-8"))
        return stringio.read()
    elif file.name.endswith(".pdf"):
        doc = fitz.open(stream=file.read(), filetype="pdf")
        return " ".join(page.get_text() for page in doc)
    return ""


# ----------- NLP Question Generation -----------

def short_answer(sentence):
    return f"❓ What is the meaning of: “{sentence}”?"


def fill_in_the_blank(sentence):
    doc = nlp(sentence)
    nouns = [token.text for token in doc if token.pos_ in ("NOUN", "PROPN")]
    if nouns:
        target = random.choice(nouns)
        blanked = sentence.replace(target, "______", 1)
        return f"✍️ Fill in the blank: {blanked}"
    return short_answer(sentence)


def generate_basic_questions(text):
    doc = nlp(text)
    sents = [sent.text.strip() for sent in doc.sents if len(sent.text) > 40]
    sampled = random.sample(sents, min(10, len(sents)))
    questions = []
    for s in sampled:
        q_type = random.choice(["short", "fill"])
        if q_type == "fill":
            q = fill_in_the_blank(s)
        else:
            q = short_answer(s)
        questions.append(q)
        if len(questions) == 5:
            break
    return questions


def generate_mcqs(text):
    try:
        input_text = f"mcq: {text}"
        result = mcq_gen(input_text, max_length=128)[0]['generated_text']
        return result
    except Exception:
        return "(⚠️ Failed to generate MCQ)"


def summarize_text(text):
    try:
        return summarizer(
            text[:1000],
            max_length=130,
            min_length=30,
            do_sample=False
        )[0]['summary_text']
    except Exception:
        return "(⚠️ Summarization failed)"


# ----------- Streamlit UI Logic -----------

uploaded = st.file_uploader(
    "Upload a .txt or .pdf file", type=["txt", "pdf"]
)

if uploaded:
    text = extract_text(uploaded)
    st.success("✅ File processed successfully.")

    with st.expander("🔍 Preview Extracted Text"):
        st.write(text[:800] + "...")

    if st.button("📄 Summarize Document"):
        summary = summarize_text(text)
        st.subheader("📌 Summary")
        st.write(summary)

    if st.button("🧠 Generate Basic Questions"):
        questions = generate_basic_questions(text)
        st.subheader("📄 Short Questions:")
        for i, q in enumerate(questions, 1):
            st.markdown(f"**Q{i}.** {q}")

    if st.button("🎯 Generate GPT/T5 MCQs"):
        st.subheader("🎓 MCQs from Document:")
        paras = text.split("\n")
        for i, p in enumerate(paras[:3]):
            if len(p.strip()) > 40:
                mcq = generate_mcqs(p.strip())
                st.markdown(f"**Q{i + 1}.** {mcq}")
