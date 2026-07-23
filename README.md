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

1. **Clone the repository:**

   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
   cd YOUR_REPOSITORY_NAME
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
