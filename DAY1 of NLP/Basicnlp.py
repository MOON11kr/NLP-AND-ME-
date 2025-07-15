import nltk
import re
import string
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer


# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')


# ------------------------
# 🔹 Input Text
# ------------------------

text = """
NLP is a fascinating field! It's all about teaching computers
to understand human language.
Sometimes, text data is messy... I
t includes punctuations, stopwords, and spelling mistakes.
Can we clean it and extract something useful? Let's try.
"""


# ------------------------
# 🔹 Text Cleaning Functions
# ------------------------

def preprocess_text(text):
    print("\n--- RAW TEXT ---")
    print(text)

    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove numbers
    text = re.sub(r'\d+', '', text)

    # Tokenize
    words = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [w for w in words if w not in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(w) for w in filtered_words]

    return {
        "clean_text": " ".join(lemmatized_words),
        "total_characters": len(text),
        "total_words": len(words),
        "filtered_words": filtered_words,
        "lemmatized_words": lemmatized_words,
        "word_freq": Counter(lemmatized_words),
        "sentences": sent_tokenize(text)
    }


# ------------------------
# 🔹 Run Preprocessing
# ------------------------

result = preprocess_text(text)


# ------------------------
# 🔹 Output Results
# ------------------------

print("\n--- CLEANED TEXT ---")
print(result["clean_text"])

print("\n--- BASIC STATS ---")
print(f"Characters: {result['total_characters']}")
print(f"Words (before stopword removal): {result['total_words']}")
print(f"Words (after stopword removal): {len(result['filtered_words'])}")
print(f"Sentences: {len(result['sentences'])}")

print("\n--- TOP 5 WORDS ---")
for word, freq in result["word_freq"].most_common(5):
    print(f"{word}: {freq}")
