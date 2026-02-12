from ingestion.pipeline import ingest_document
from rag.query_engine import query_rag
import os


# First ingest
if os.path.exists("data/docs/knowledge_base.pdf"):
    ingest_document("data/docs/knowledge_base.pdf")
else:
    print("\n⚠ No knowledge_base.pdf found. Skipping ingestion.")
    print("Add a PDF to data/docs/ and run again, or use inspect_db.py to check existing data.\n")


print("\n" + "=" * 60)
print("RAG QUERY INTERFACE")
print("=" * 60)
print("Commands:")
print(" - Type your question to query the database")
print(" - Type 'verbose' to toggle detailed output")
print(" - Type 'quit' or 'exit' to stop")
print("=" * 60 + "\n")


verbose = False

while True:
    try:
        q = input("\n💬 Ask something: ")

        if q.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        if q.lower() == "verbose":
            verbose = not verbose
            print(f"Verbose mode: {'ON' if verbose else 'OFF'}")
            continue

        if q.strip():
            print("\n" + "=" * 60)
            answer = query_rag(q, verbose=verbose)

            if not verbose:
                print("\n📌 Answer:\n")

            print(answer)
            print("=" * 60)

    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        break

    except Exception as e:
        print(f"\n❌ Error: {e}")
