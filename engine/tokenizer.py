import re
import os
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

ps = PorterStemmer()
STOP_WORDS = set(stopwords.words("english"))

def tokenize(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    words = text.split()

    # remove stop-words + apply stemming
    tokens = [ps.stem(w) for w in words if w not in STOP_WORDS]
    return tokens

def read_documents(folder_path):
    documents = {}
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as file:
                text = file.read()
                documents[filename] = tokenize(text)
    
    return documents
