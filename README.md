# 🔍 Mini Search Engine with TF–IDF Ranking

This project is a lightweight search engine built from scratch in Python that ranks text documents based on their relevance to a user query using **TF–IDF (Term Frequency–Inverse Document Frequency)** and **Cosine Similarity**.

The system demonstrates core concepts from **Information Retrieval, Algorithms, and Data Processing**, making it a strong computer science side project.

---

## 🚀 Features

- 📄 Reads multiple text documents from a folder  
- 🧹 Text preprocessing:
  - Lowercasing  
  - Punctuation removal  
  - Stop-word removal  
  - Stemming (Porter Stemmer via NLTK)  
- 📊 Represents documents using **TF–IDF vectors**  
- 📐 Ranks documents using **Cosine Similarity**  
- 💬 Interactive command-line search interface  

---

## 🧠 How It Works

1. **Tokenization** – cleans and normalizes text  
2. **TF–IDF Computation** – assigns importance to words  
3. **Query Processing** – converts user query into a TF–IDF vector  
4. **Ranking** – compares query vector with document vectors using cosine similarity  

---

## 📁 Project Structure

mini-search-engine/
│
├── data/
│ ├── doc1.txt
│ ├── doc2.txt
│ ├── doc3.txt
│ └── doc4.txt
│
├── engine/
│ ├── init.py
│ ├── tokenizer.py
│ ├── tfidf.py
│ └── ranker.py
│
└── main.py


---

## ▶️ How to Run

### Step 1 — Install dependencies

```bash
pip install nltk
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
``` 
python main.py
Enter your search query: computer data communication
Search Results:
doc2.txt -> 0.276
doc4.txt -> 0.029
doc1.txt -> 0.0
doc3.txt -> 0.0
