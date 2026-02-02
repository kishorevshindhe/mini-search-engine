import math
from collections import defaultdict

def compute_tf(doc_tokens):
    tf = defaultdict(int)
    for word in doc_tokens:
        tf[word] += 1

    total_words = len(doc_tokens)
    for word in tf:
        tf[word] = tf[word] / total_words
    return tf

def compute_idf(all_documents):
    N = len(all_documents)
    idf = defaultdict(float)
    doc_frequency = defaultdict(int)

    for tokens in all_documents.values():
        unique_words = set(tokens)
        for word in unique_words:
            doc_frequency[word] += 1

    for word, df in doc_frequency.items():
        idf[word] = math.log(N / (1 + df))

    return idf

def compute_tfidf(documents):   # ← THIS MUST EXIST
    idf = compute_idf(documents)
    tfidf_scores = {}

    for doc_name, tokens in documents.items():
        tf = compute_tf(tokens)
        tfidf = {}

        for word, tf_val in tf.items():
            tfidf[word] = tf_val * idf[word]

        tfidf_scores[doc_name] = tfidf

    return tfidf_scores
