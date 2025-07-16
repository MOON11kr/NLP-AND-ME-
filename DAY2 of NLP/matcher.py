# matcher.py

import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    tokens = word_tokenize(text)
    filtered = [
        lemmatizer.lemmatize(w) for w in tokens if w not in stop_words
    ]
    return filtered


def match_keywords(resume_text, keywords_list):
    resume_tokens = set(clean_text(resume_text))

    keyword_tokens = [clean_text(kw) for kw in keywords_list]
    keyword_flat = set(
        [item for sublist in keyword_tokens for item in sublist]
    )

    matched = resume_tokens & keyword_flat
    unmatched = keyword_flat - matched

    score = (
        round(len(matched) / len(keyword_flat) * 100, 2)
        if keyword_flat else 0.0
    )

    return {
        "matched": sorted(matched),
        "unmatched": sorted(unmatched),
        "score": score
    }
