# versioning/chromadb_manager.py

import chromadb
import uuid
import os
from datetime import datetime

# Initialize ChromaDB persistent client
client = chromadb.PersistentClient(path=os.path.join(os.getcwd(), "data", "versions", "chroma"))
collection = client.get_or_create_collection("book_versions")


def save_version(text):
    """
    Saves the finalized version to ChromaDB with auto-incremented version label.
    """
    # Determine the next version label based on existing count
    existing = collection.get(include=["metadatas"])
    count = len(existing['metadatas'])
    version_label = f"v{count + 1}"

    doc_id = str(uuid.uuid4())
    metadata = {
        "version_name": version_label,
        "timestamp": datetime.utcnow().isoformat()
    }

    collection.add(documents=[text], ids=[doc_id], metadatas=[metadata])
    print(f"✅ Saved as version {version_label} with ID: {doc_id}")


def get_all_versions():
    """
    Returns all stored versions from ChromaDB.
    """
    results = collection.get(include=["documents", "metadatas"])
    results["ids"] = results.pop("ids", []) #preserve if available, fallback to empty
    return results


def list_versions():
    """
    Prints all versions with metadata in CLI.
    """
    results = get_all_versions()
    documents = results.get("documents", [])
    metadatas = results.get("metadatas", [])
    ids = results.get("ids", [])

    if not documents:
        print("❌ No versions saved yet.")
        return

    print("\n📚 Saved Versions:")
    for i, (meta, doc_id) in enumerate(zip(metadatas, ids), 1):
        version_label = (meta or {}).get('version_name', f'version-{i}')
        timestamp = (meta or {}).get('timestamp', 'N/A')

        print(f"\n🔖 {version_label}")
        print(f"🆔 ID: {doc_id}")
        print(f"📅 Timestamp: {timestamp}")
        print(f"📝 Preview:\n{documents[i-1][:300]}...")