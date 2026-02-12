# OP-codex

Local Retrieval-Augmented Generation (RAG) pipeline using:

* Sentence Transformers (embeddings)
* ChromaDB (vector database)
* Ollama (LLM)
* PDF ingestion

Runs fully local.

---

# Requirements

* Windows 10/11 (64-bit)
* Python 3.10 or 3.11
* 8GB+ RAM
* Ollama installed

---

# Setup

## 1. Create Virtual Environment

```bash
python -m venv env
```

Activate:

```bash
env\Scripts\activate
```

---

## 2. Install Dependencies

Use pinned versions (important for compatibility):

```bash
pip install -r requirements.txt
```

Recommended `requirements.txt`:

```
sentence-transformers==2.2.2
chromadb==0.4.22
pypdf==3.17.4
ollama==0.1.6
huggingface_hub==0.14.1
numpy==1.26.4
```

Do not upgrade randomly — it will break.

---

# Install Ollama

1. Download from:
   [https://ollama.com/download](https://ollama.com/download)

2. Install normally.

3. Pull model:

```bash
ollama pull mistral
```

4. Verify:

```bash
ollama list
```

You should see:

```
mistral
```

Note: On Windows, Ollama runs as a background service automatically.

---

# Add Document

Place your PDF inside:

```
data/docs/sample.pdf
```

---

# Run

Activate environment:

```bash
env\Scripts\activate
```

Run:

```bash
python app.py
```

---

# Troubleshooting

### WinError 10061

Ollama is not running.
Open Ollama or restart your PC.

Test:

```bash
ollama list
```

---

### NumPy error (`np.float_ removed`)

```bash
pip install numpy==1.26.4
```

---

### cached_download error

```bash
pip install huggingface_hub==0.14.1
```

---

# Reset Database

Delete:

```
chroma_db/
```

Then run `app.py` again.

---