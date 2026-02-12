from sentence_transformers import SentenceTransformer
import chromadb
import ollama

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("project_docs")


def query_rag(question, top_k=3, verbose=False):

    if verbose:
        print(f"\n🔎 Searching vector DB for: '{question}'")

    query_embedding = embed_model.encode([question]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    if verbose:
        print(f"✔ Found {len(results['documents'][0])} relevant chunks")
        print("\n📚 Retrieved context:")
        for i, doc in enumerate(results["documents"][0]):
            print(f"[{i+1}] {doc[:80]}...")

    context = "\n".join(results["documents"][0])

    prompt = f"""
Use ONLY the context below to answer:

Context:
{context}

Question:
{question}
"""

    if verbose:
        print("\n🤖 Generating answer with Ollama...")

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
