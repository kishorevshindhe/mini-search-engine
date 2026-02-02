from engine.tokenizer import read_documents
from engine.tfidf import compute_tfidf, compute_idf
from engine.ranker import rank_documents

documents = read_documents("data")

idf = compute_idf(documents)
tfidf_scores = compute_tfidf(documents)

query = input("\nEnter your search query: ")

results = rank_documents(query, tfidf_scores, idf)

print("\nSearch Results:")
for doc, score in results:
    print(f"{doc} -> {round(score, 3)}")
