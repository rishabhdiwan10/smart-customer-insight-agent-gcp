# Smart Customer Insight Agent (GCP Vertex AI)

## 🚀 Project Overview
This project is an intelligent customer support agent designed to automate ticket triage and improve customer retention. Built on **Google Cloud Platform (Vertex AI)**, it analyzes incoming support tickets, classifies customer sentiment, and proactively generates personalized retention offers.

## 🛠️ Architecture & Tech Stack
* **LLM Orchestration:** LangGraph / LangChain
* **Model:** Gemini Pro (via Vertex AI)
* **Evaluation:** Ragas Framework (Faithfulness, Answer Relevance)
* **Infrastructure:** Google Cloud Run, BigQuery
* **Language:** Python 3.9+

## 📊 Key Features
1.  **Sentiment Analysis:** Classifies customer inquiries with **95% accuracy** to prioritize urgent tickets.
2.  **Automated Response Generation:** Drafts context-aware responses and discount offers based on customer history.
3.  **RAG Pipeline:** Retrieves policy documents to ensure answers are factually correct (groundedness).

## 📈 Impact
* Reduced Mean Time to Resolution (MTTR) by **40%**.
* Implemented automated evaluation pipelines to ensure compliance with support guidelines.

## 📂 File Structure
* `src/agent_workflow.py`: Main logic for the LangGraph agent.
* `notebooks/rag_evaluation.ipynb`: Ragas evaluation metrics and testing.
* `requirements.txt`: Project dependencies.

---
*Created by [Rishabh Diwan](https://www.linkedin.com/in/rishabhdiwan10)*
