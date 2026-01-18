# 🔍 RaFT-Based Dataset Enrichment for Interviewer Model Fine-Tuning

This repository implements a **Retrieval-augmented Fine-Tuning (RaFT) pipeline** for enriching question–answer datasets with **high-quality, concept-grounded context**, designed specifically for training **AI interviewer models**.

## 🧠 Motivation and Impact

In building an AI interviewer, a key challenge is ensuring that the model **remains conceptually grounded** and can ask relevant, insightful follow-up questions. Traditional QA datasets often provide only questions and answers, which leads to models that:

- Memorize surface-level patterns without true understanding
- Generate repetitive or generic follow-ups
- Miss connections between related concepts
- Hallucinate or provide incomplete reasoning

To address these issues, we developed a **Retrieval-augmented Fine-Tuning (RaFT) pipeline** that enriches datasets with **concept-level, merged context** derived from a structured knowledge base. By pairing each question with rich, interviewer-style contextual information, the model gains:

- Consistent exposure to domain knowledge
- Awareness of trade-offs, best practices, and common mistakes
- Concept-level reasoning aligned with human experts

This approach bridges the gap between **raw datasets** and **expert-level interviewer behavior**, producing supervision data that is both **scalable and high quality**.

---

## ⚡ Before vs After Example

### Before RaFT Enrichment
| Question | Ideal Answer |
|----------|--------------|
| Explain polymorphism in OOP. | Polymorphism allows objects of different classes to be treated as objects of a common superclass. |

**Observation:**  
- Model trained on this data tends to give **shallow answers**, may ignore edge cases, and rarely connects related concepts like inheritance or interface design.

---

### After RaFT Enrichment
| Question | Ideal Answer | Detailed Context |
|----------|--------------|----------------|
| Explain polymorphism in OOP. | Polymorphism allows objects of different classes to be treated as objects of a common superclass. | **Concept: Polymorphism**  
Polymorphism is a core OOP principle enabling objects to take many forms. It allows method overriding and interface implementation. Key benefits include flexible code, reduced duplication, and easier maintenance. Common mistakes include confusing polymorphism with inheritance. Follow-Up Prompts: 1. Explain why this concept is important. 2. Provide a code example demonstrating it. 3. Describe common mistakes developers make. 4. Discuss trade-offs and best practices. |

**Observation:**  
- Model now receives **rich, concept-grounded context**  
- Can reason about trade-offs, provide code examples, and generate meaningful follow-ups  
- Reduces hallucination and improves answer quality during fine-tuning

---

This example illustrates how the RaFT pipeline transforms a basic QA dataset into **training data suitable for a concept-aware AI interviewer**, bridging the gap between surface-level answers and deep conceptual understanding.

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
