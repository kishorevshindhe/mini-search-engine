# Mini Search Engine with TF-IDF Ranking

This project is a lightweight search engine made from scratch in Python. It ranks text documents based on how relevant they are to a user query using **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Cosine Similarity**.

The system shows basic ideas from **Information Retrieval, Algorithms, and Data Processing**. This makes it a valuable computer science side project.

---

##  Features
- Multiple text files from a directory are read.  
- The following text preprocessing steps take place:
  - Convert to lowercase
  - Remove punctuation
  - Remove stop words
  - Stem words using the Porter Stemmer (via NLTK)
- Writes documents as **TF–IDF vectors**  
- Documents are ranked using **Cosine Similarity**  
- An interactive search command-line interface is available.
---

##  How It Works

1. **Tokenization** – cleans and normalizes text  
2. **TF–IDF Computation** – assigns importance to words  
3. **Query Processing** – converts user query into a TF–IDF vector  
4. **Ranking** – compares query vector with document vectors using cosine similarity  

---

---

##  How to Run

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

Learning Objectives

This project gave me the following benefits:
-A practical comprehension of information retrieval
-Experience implementing TF–IDF from scratch
-An understanding of text data's vector representation
-Hands-on experience with cosine similarity ranking
-a more solid foundation in data processing and algorithms

In order to improve my systems-level and algorithmic knowledge for graduate computer science studies, this project was created as a fundamental computer science side project.
