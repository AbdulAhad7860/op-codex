"""
Interactive ChromaDB Inspector
Inspect and verify the contents of your vector database
"""

import chromadb
from sentence_transformers import SentenceTransformer


def main():
    print("\n" + "=" * 60)
    print("CHROMADB INSPECTOR")
    print("=" * 60 + "\n")

    try:
        client = chromadb.PersistentClient(path="./chroma_db")
        print("✔ Connected to ChromaDB at ./chroma_db/")
    except Exception as e:
        print(f"❌ Failed to connect to ChromaDB: {e}")
        return

    # List all collections
    collections = client.list_collections()
    print(f"\nCollections found: {len(collections)}")

    if not collections:
        print("\n⚠ No collections found. Run app.py to ingest documents first.")
        return

    for coll in collections:
        print(f" - {coll.name}")

    # Focus on project_docs collection
    try:
        collection = client.get_collection("project_docs")
        print("\n" + "=" * 60)
        print("COLLECTION: project_docs")
        print("=" * 60)

        # Get count
        count = collection.count()
        print(f"\n📦 Total documents: {count}")

        if count == 0:
            print("\n⚠ Collection is empty. Run app.py to ingest documents.")
            return

        # Get all data
        print("\nFetching all documents...")
        results = collection.get()

        # Show sample documents
        print("\n" + "=" * 60)
        print("SAMPLE DOCUMENTS (first 5):")
        print("=" * 60)

        for i, (doc_id, doc_text) in enumerate(
            zip(results["ids"][:5], results["documents"][:5])
        ):
            print(f"\n[{i+1}] ID: {doc_id}")
            print(
                f"Text: {doc_text[:150]}{'...' if len(doc_text) > 150 else ''}"
            )

        # Interactive search
        print("\n" + "=" * 60)
        print("INTERACTIVE SEARCH")
        print("=" * 60)
        print("Search your vector database (type 'quit' to exit)\n")

        embed_model = SentenceTransformer("all-MiniLM-L6-v2")

        while True:
            query = input("🔎 Search query: ").strip()

            if query.lower() in ["quit", "exit", "q"]:
                break

            if not query:
                continue

            # Search
            query_embedding = embed_model.encode([query]).tolist()

            search_results = collection.query(
                query_embeddings=query_embedding,
                n_results=3,
            )

            print(f"\n🔝 Top 3 results for: '{query}'")
            print("=" * 60)

            for i, (doc, distance) in enumerate(
                zip(
                    search_results["documents"][0],
                    search_results["distances"][0]
                    if "distances" in search_results
                    else [0] * 3,
                )
            ):
                print(f"\n[{i+1}] Similarity score: {1 - distance:.4f}")
                print(
                    f"{doc[:200]}{'...' if len(doc) > 200 else ''}"
                )

            print()

        print("\nGoodbye!")

    except Exception as e:
        print(f"\n❌ Error accessing collection: {e}")
        print("Make sure you've run app.py to create the collection first.")


if __name__ == "__main__":
    main()
