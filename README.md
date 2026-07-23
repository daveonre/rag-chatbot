# 🤖 RAG Chatbot with FastAPI, React & Docker

A full-stack Retrieval-Augmented Generation (RAG) application that allows users to upload custom PDF documents and ask questions based on their contents using LLMs and vector search.

> ⚠️ **Disclaimer:** This is a **test and experimental project** that is actively under development. Document parsing, chunking, and context retrieval may not handle all edge cases smoothly and might contain bugs or errors. Features are continuously being updated and improved.

---

## ✨ Features

- **📄 Document Ingestion:** Upload and process PDF documents into vector embeddings.
- **🔍 Contextual Retrieval:** Uses ChromaDB vector search to retrieve relevant document chunks.
- **💬 RAG Question Answering:** Powered by a FastAPI backend and LLMs to generate context-aware answers.
- **🐳 Fully Containerized:** Microservices orchestration using Docker Compose and NGINX as a reverse proxy.

---

## 🛠️ Tech Stack

- **Frontend:** React, Vite, Axios
- **Backend:** FastAPI, Python, Uvicorn
- **Database / Vector Store:** ChromaDB / MongoDB
- **Reverse Proxy:** NGINX
- **Containerization:** Docker & Docker Compose

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed on your machine:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Git](https://git-scm.com/)

---

### 📥 Installation & Setup

1. **Clone this repository:**

   ```bash
   git clone https://github.com/USERNAME/REPOSITORY_NAME.git
   cd REPOSITORY_NAME
   ```

2. **Set up Environment Variables:**
   Copy the example environment file and add your credentials:

   ```bash
   cp .env.example .env
   ```

   Open `.env` and fill in your required API keys (e.g., `OPENAI_API_KEY`).

3. **Run the Application with Docker Compose:**

   ```bash
   docker compose up --build -d
   ```

4. **Access the App:**
   Open your browser and navigate to:
   - **Frontend Application:** `http://localhost:3000`
   - **FastAPI Docs:** `http://localhost:8000/docs`

---

## 📄 Sample Test PDF & Example Questions

A sample policy handbook (`sample_document.pdf`) is provided in the root directory so you can test the RAG ingestion, vector embedding, and response generation immediately.

### 1. Upload the Sample PDF

1. Open the web interface at `http://localhost:3000`.
2. Upload `sample_document.pdf` from the project root folder.

### 2. Verify Retrieval & Generation

Once the document is processed and indexed, ask the AI assistant these questions to verify that the RAG pipeline retrieves the correct chunks:

- 🕒 **"What are the core working hours?"**
- 🏠 **"How many days can employees work remotely?"**
- 🌴 **"What is the policy on rolling over unused PTO?"**
- 🔒 **"What are the software installation and encryption requirements?"**

---

## 🛠️ Project Architecture

```text
├── backend/            # FastAPI Application
│   ├── app/            # Routers, Models, Services (Embeddings, LLM, Retrieval)
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/           # React Frontend Application
│   ├── src/            # React Components & API handlers
│   ├── nginx.conf      # NGINX configuration
│   └── Dockerfile
├── docker-compose.yml  # Docker multi-container setup
├── .env.example        # Environment variables template
└── README.md
```

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.
