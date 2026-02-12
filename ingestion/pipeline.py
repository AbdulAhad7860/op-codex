from ingestion.loader import load_pdf
from ingestion.chunker import chunk_text
from ingestion.embedder import embed_chunks
from vector_store.chroma_store import store_chunks


def ingest_document(path):
    print("\n" + "=" * 60)
    print("STARTING DOCUMENT INGESTION")
    print("=" * 60)

    print(f"\n📄 Loading document: {path}")
    text = load_pdf(path)
    print(f"✔ Loaded {len(text)} characters")

    print("\n✂ Chunking text...")
    chunks = chunk_text(text)
    print(f"✔ Created {len(chunks)} chunks")
    print(f"✔ Average chunk size: {sum(len(c) for c in chunks) // len(chunks)} chars")
    print(f"✔ Sample chunk: {chunks[0][:100]}...")

    print("\n🧠 Generating embeddings...")
    embeddings = embed_chunks(chunks)
    print(f"✔ Generated {len(embeddings)} embeddings")
    print(f"✔ Embedding dimension: {len(embeddings[0])}")

    print("\n💾 Storing in ChromaDB...")
    stored_count = store_chunks(chunks, embeddings)
    print(f"✔ Stored {stored_count} documents in vector database")
    print("✔ Location: ./chroma_db/")
    print("✔ Collection: project_docs")

    print("\n" + "=" * 60)
    print("✅ INGESTION COMPLETE!")
    print("=" * 60 + "\n")
