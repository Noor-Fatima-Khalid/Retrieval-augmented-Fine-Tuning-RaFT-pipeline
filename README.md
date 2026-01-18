# 🔍 RaFT-Based Dataset Enrichment for Interviewer Model Fine-Tuning

This repository implements a **Retrieval-augmented Fine-Tuning (RaFT) pipeline** for enriching question–answer datasets with **high-quality, concept-grounded context**, designed specifically for training **AI interviewer models**.

## 🧠 Motivation and Impact

In building an AI interviewer, a key challenge is ensuring that the model **remains conceptually grounded** and can ask relevant, insightful follow-up questions. We crafted a dataset that had this format: Context | Difficulty | Questions | Ideal Answers. The context only contained keywords of other approaches that could be used to answer the question. It lead the model to:
- Memorize surface-level patterns without true understanding
- Generate repetitive or generic follow-ups
- Miss connections between related concepts
- Hallucinate/provide incomplete reasoning

To address these issues, We made a comprehensive knowledge base of all the domains. Then we developed a **Retrieval-augmented Fine-Tuning (RaFT) pipeline** that enriches datasets with **concept-level, merged context** derived from the structured knowledge base. Each topic in the knowledge base is based on this template:
- Name: The concept/topic 
- Category: Core principle / Relationship / Design Pattern / Best Practice
- Difficulty: Easy / Medium / Hard 
- Tags: Keywords for retrieval 
- Definition: Formal explanation of the concept.
- Key Properties: Essential characteristics or rules.
- Related Concepts: Links to other concepts
= How to Implement: Step-by-step guidance for applying the concept in code.
- Variants / Language Differences: Any language-specific considerations (e.g., in OOP: C++ destructors, Java interfaces).
- Common Patterns: Typical ways the concept is used in real projects
- Why It Exists: Explain the motivation behind the concept.
- Trade-offs: Pros/cons, alternatives, or pitfalls if misused.
- Best Practices: Recommendations for correct usage.
- Code Snippet: Example demonstrating the concept. Include comments explaining reasoning.
- Real-World Analogy: Optional but helps reasoning and context retrieval.
- Common Mistakes: Things developers frequently get wrong.
- Consequences: Why mistakes are bad.
- How to Avoid: Tips or rules to prevent misuse.
- Questions the concept can answer: Helpful for retrieval-augmented pipelines.
- Cross-concept connections: How this concept interacts with others (useful for embeddings).

By pairing each question with rich, interviewer-style contextual information, the model gains:
- Consistent exposure to domain knowledge
- Awareness of trade-offs, best practices, and common mistakes
- Concept-level reasoning aligned with human experts

The pipeline takes:
- A **domain-specific knowledge base** (concept-structured text)
- A **question dataset** (Excel `.xls/.xlsx`)
- And produces **rich, merged, concept-aware context** for every question

The enriched context is written back into the dataset as a new column, making it directly usable for **context-aware fine-tuning**.

---

## ✨ What This Pipeline Does

- Chunks a knowledge base by **concept and semantic sections**
- Embeds chunks using **Sentence Transformers**
- Indexes them with **FAISS** for fast semantic retrieval
- Retrieves the most relevant concepts for each question
- Merges and deduplicates retrieved content
- Appends structured **interviewer-style follow-up prompts**
- Writes the result into a new dataset column:  
  **`detailed-context`**

All processing is done locally and is **model-agnostic**.

---

## 📊 Input Dataset Format

The pipeline expects an Excel dataset with at least the following columns:

| Column | Description |
|------|------------|
| `Questions` | Interview or assessment questions |
| `Ideal Answers` | Reference answers (optional but supported) |

Additional columns (e.g. Difficulty, Topic, Context) are preserved.

---

## 📤 Output

The output is a **non-destructive enriched Excel file** containing all original columns plus:

| New Column | Description |
|----------|------------|
| `detailed-context` | Retrieved, merged, concept-grounded context per question |

This output is suitable for:
- Supervised fine-tuning
- Instruction tuning
- RAG evaluation datasets
- Interview simulation models

---

## 🧠 Why RaFT?

Unlike naive RAG pipelines, this approach:
- Grounds each question in **explicit conceptual knowledge**
- Avoids shallow keyword matching
- Reduces hallucinations during fine-tuning
- Produces **stable, reusable supervision data**

This is especially effective for **technical interviewers**, **assessment bots**, and **domain-specific LLMs**.

---

## 🛠 Tech Stack

- `sentence-transformers`
- `FAISS`
- `NLTK`
- `pandas`
- `tqdm`
- Google Colab / Python 3.10+

---

## 🎯 Use Cases

- Training AI interviewers  
- Enriching technical QA datasets  
- Curriculum-aligned model fine-tuning  
- Knowledge-grounded instruction datasets  
- LLM evaluation and probing  

---

## 🚀 Status

This project is **production-ready for dataset enrichment** and scales cleanly to hundreds of questions and thousands of knowledge chunks.
