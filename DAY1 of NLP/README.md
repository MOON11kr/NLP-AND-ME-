# 🧠 Day 1: Basic NLP Text Preprocessing

This project demonstrates a simple but essential NLP pipeline in Python using NLTK. It processes raw text through several key steps such as tokenization, stopword removal, lemmatization, and word frequency analysis.

---

## 🔍 Features

- ✅ Converts text to lowercase  
- ✅ Removes punctuation and digits  
- ✅ Tokenizes into words and sentences  
- ✅ Removes English stopwords  
- ✅ Lemmatizes remaining words  
- ✅ Counts frequency of words  
- ✅ Shows sentence and character stats

---

## 📦 Requirements

Install required packages (Python 3.7+ recommended):

```bash
pip install nltk

# to install during run time use 
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

#run the project
python Basicnlp.py



