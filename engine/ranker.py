import math
from engine.tokenizer import tokenize

def cosine_similarity(vec1, vec2):
    common_words = set(vec1.keys()) & set(vec2.keys())

    numerator = sum(vec1[w] * vec2[w] for w in common_words)

    sum1 = sum(v ** 2 for v in vec1.values())
    sum2 = sum(v ** 2 for v in vec2.values())

    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if denominator == 0:
        return 0

    return numerator / denominator

def rank_documents(query, tfidf_scores, idf):
    query_tokens = tokenize(query)

    from collections import Counter
    query_tf = Counter(query_tokens)
    total = len(query_tokens)

    # IMPORTANT: query is now also TF–IDF
    query_vec = {
        w: (query_tf[w] / total) * idf.get(w, 0)
        for w in query_tf
    }

    rankings = []

    for doc, doc_vec in tfidf_scores.items():
        score = cosine_similarity(query_vec, doc_vec)
        rankings.append((doc, score))

    rankings.sort(key=lambda x: x[1], reverse=True)
    return rankings
