import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load model and data
@st.cache_resource
def load_model_and_data():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    df = pd.read_csv("quotes.csv")  # Replace with your path or download step
    embeddings = np.load("quote_embeddings.npy")  # Precomputed FAISS index vectors
    return model, df, embeddings

model, df, embeddings = load_model_and_data()

# Load FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

st.title("📚 Quote Retrieval App (RAG-style)")
query = st.text_input("Ask something like: quotes about courage by Oscar Wilde")

if query:
    query_embedding = model.encode([query])
    D, I = index.search(query_embedding, k=5)
    
    results = df.iloc[I[0]]
    for i, row in results.iterrows():
        st.write(f"**Quote:** {row['quote']}")
        st.write(f"_Author:_ {row['author']}")
        st.write(f"_Tags:_ {row['tags']}")
        st.markdown("---")
