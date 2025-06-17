# rl_search/retriever.py

from versioning.chromadb_manager import get_all_versions
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def retrieve_version(query, top_k=1):
    """
    Basic RL-inspired retrieval: vectorizes documents and query using TF-IDF,
    then finds most similar entries based on cosine similarity.
    """
    versions = get_all_versions()
    documents = versions.get("documents", [])
    ids = versions.get("ids", [])
    metadatas = versions.get("metadatas", [])

    if not documents:
        print("❌ No versions found in ChromaDB.")
        return None

    vectorizer = TfidfVectorizer().fit(documents + [query])
    doc_vecs = vectorizer.transform(documents)
    query_vec = vectorizer.transform([query])

    similarities = (doc_vecs @ query_vec.T).toarray().ravel()
    top_indices = similarities.argsort()[::-1][:top_k]

    results = []
    for idx in top_indices:
        results.append({
            "id": ids[idx],
            "content": documents[idx],
            "score": similarities[idx],
            "metadata": metadatas[idx]
        })
    return results
