# keywords.py

# 🔹 Machine Learning & Data Science
ML_KEYWORDS = [
    "python", "machine learning", "data analysis", "deep learning",
    "tensorflow", "pytorch", "scikit-learn", "pandas", "numpy",
    "matplotlib", "seaborn", "data preprocessing", "model evaluation",
    "classification", "regression", "clustering", "data visualization"
]

# 🔹 Web Development
WEBDEV_KEYWORDS = [
    "html", "css", "javascript", "react", "node.js", "express.js",
    "mongodb", "sql", "postgresql", "api development", "rest api",
    "git", "github", "deployment", "responsive design"
]

# 🔹 Natural Language Processing
NLP_KEYWORDS = [
    "nlp", "text preprocessing", "tokenization", "stemming",
    "lemmatization", "named entity recognition", "text classification",
    "sentiment analysis", "word embeddings", "transformers",
    "bert", "gpt", "topic modeling", "language modeling"
]

# 🔹 Soft Skills
SOFT_SKILLS = [
    "communication", "teamwork", "leadership", "adaptability",
    "time management", "critical thinking", "problem solving",
    "presentation", "collaboration", "decision making",
    "project management"
]

# 🔹 Tools & Platforms
TOOLS_KEYWORDS = [
    "jupyter notebook", "colab", "vs code", "docker", "kubernetes",
    "aws", "azure", "google cloud", "linux", "bash", "terminal"
]


# ✅ Optional: Combine all
def get_all_keywords():
    return (
        ML_KEYWORDS + WEBDEV_KEYWORDS + NLP_KEYWORDS +
        SOFT_SKILLS + TOOLS_KEYWORDS
    )
