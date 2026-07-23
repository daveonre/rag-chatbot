import axios from "axios";

// The URL where your FastAPI server is running
const API_BASE_URL = "http://127.0.0.1:8000";

const api = axios.create({
  // baseURL: API_BASE_URL,
  baseURL: "",
});

/**
 * Sends uploaded PDF files to /api/documents/upload
 */
export const uploadDocuments = async (files) => {
  const formData = new FormData();
  for (let i = 0; i < files.length; i++) {
    formData.append("files", files[i]);
  }

  const response = await api.post("/api/documents/upload", formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
  return response.data;
};

/**
 * Sends a question to /api/chat/ and gets back an answer + context chunks
 */
export const askQuestion = async (question, topK = 3) => {
  const response = await api.post("api/chat/", {
    question,
    top_k: topK,
  });
  return response.data;
};
