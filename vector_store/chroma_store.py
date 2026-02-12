import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("project_docs")


def store_chunks(chunks, embeddings):
    # Get current count before adding
    current_count = collection.count()

    # Generate IDs starting from current count to avoid duplicates
    ids = [f"doc_{current_count + i}" for i in range(len(chunks))]

    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=chunks
    )

    # Return new total count
    new_count = collection.count()
    return new_count
