import os
import pandas as pd
from tqdm import tqdm
import faiss
from sentence_transformers import SentenceTransformer
import nltk
import json

from chunking import chunk_kb_by_concept_clean
from cleaning import clean_chunk_text
from retrieval import generate_interviewer_context

# Download NLTK punkt
nltk.download("punkt")

# --------------------------
# CONFIG
# --------------------------
KB_PATH = "KB/Knowledge Base.txt"        # local knowledge base
DATASET_PATH = "dataset/oop_questions.xlsx"  # local dataset
OUTPUT_PATH = "dataset/oop_dataset_with_detailed_context.xlsx"

# --------------------------
# LOAD KNOWLEDGE BASE
# --------------------------
with open(KB_PATH, "r", encoding="utf-8") as f:
    KB_TEXT = f.read()

# --------------------------
# LOAD DATASET
# --------------------------
df = pd.read_excel(DATASET_PATH)
df.columns = df.columns.str.strip().str.lower()  # normalize column names

if "questions" not in df.columns:
    raise ValueError(f"'questions' column not found. Columns: {df.columns.tolist()}")

# --------------------------
# INITIALIZE EMBEDDING MODEL
# --------------------------
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# --------------------------
# CHUNK KB & BUILD FAISS INDEX
# --------------------------
kb_chunks, kb_metadata = chunk_kb_by_concept_clean(KB_TEXT)
kb_chunks = [clean_chunk_text(c) for c in kb_chunks]

chunk_embeddings = embedder.encode(kb_chunks, convert_to_numpy=True)
dim = chunk_embeddings.shape[1]

index = faiss.IndexFlatL2(dim)
index.add(chunk_embeddings)

print(f"FAISS index built with {index.ntotal} chunks.")

# --------------------------
# GENERATE DETAILED CONTEXT
# --------------------------
detailed_contexts = []

for question in tqdm(df["questions"], desc="Generating detailed context"):
    context = generate_interviewer_context(question, k=8)
    detailed_contexts.append(context)

df["detailed-context"] = detailed_contexts

# --------------------------
# SAVE OUTPUT
# --------------------------
df.to_excel(OUTPUT_PATH, index=False)
print(f"✅ Enriched dataset saved to {OUTPUT_PATH}")

