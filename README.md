# 🧠 RAG-Based Semantic Quote Retrieval and Structured QA

## 🔍 Objective
This project demonstrates a **Retrieval-Augmented Generation (RAG)** pipeline for semantic quote retrieval using the [Abirate/english_quotes](https://huggingface.co/datasets/Abirate/english_quotes) dataset.

Users can enter natural language queries like:
> _“Show me quotes about courage by women authors”_

The system responds with relevant quotes, authors, tags, and similarity scores in a structured format.

---

## 📚 Dataset
- Source: Hugging Face → [`Abirate/english_quotes`](https://huggingface.co/datasets/Abirate/english_quotes)
- Fields:
  - `quote` – the quote text
  - `author` – who said it
  - `tags` – topics/keywords

---

## 🧹 Step 1: Data Preparation
- Load the `.jsonl` dataset using `pandas`
- Preprocess:
  - Remove missing rows
  - Normalize quotes (lowercasing, strip punctuation)
  - Flatten tag lists into comma-separated strings

---

## 🔧 Step 2: Model Fine-Tuning
- Model used: `all-MiniLM-L6-v2` from Sentence Transformers
- Fine-tuned using `InputExample` pairs like:
  > Query: "inspirational quotes" ↔ Quote: "be yourself; everyone else is already taken."
- Framework: `sentence-transformers`
- Output: Saved model directory `quote-retriever-model/`

---

## 📦 Step 3: Indexing for Retrieval
- Library: `FAISS`
- Encoded all quotes using the fine-tuned model
- Built a vector index (`quotes.index`) for fast semantic search

---

## 🤖 Step 4: RAG Integration
- Retrieved quote contexts using FAISS
- Passed results to a language model (e.g., OpenAI GPT or open-source LLM)
- Generated enriched, contextual responses

---

## 📊 Step 5: RAG Evaluation
- Used frameworks like:
  - `RAGAS`
  - `Quotient`
  - `Arize Phoenix`
- Evaluation based on relevance, coverage, and factual accuracy

---

## 🌐 Step 6: Streamlit App
- Interactive UI for end-users
- Input: Natural language queries
- Output:
  - Matching quotes, authors, tags
  - Optional similarity score
  - JSON-style response

---

# IMP:  it needs a Open api key also so you can use your key