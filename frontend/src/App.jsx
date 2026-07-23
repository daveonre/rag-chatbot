import React, { useState } from "react";
// 1. Import the functions we wrote in app.js
import { uploadDocuments, askQuestion } from "./app";

export default function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [uploading, setUploading] = useState(false);

  // 2. Function to handle document uploads
  const handleFileUpload = async (e) => {
    const selectedFiles = Array.from(e.target.files);
    if (selectedFiles.length === 0) return;

    setUploading(true);
    try {
      const data = await uploadDocuments(selectedFiles);
      alert(`Success! Indexed ${data.total_files} file(s).`);
    } catch (err) {
      alert("Upload failed! Make sure FastAPI is running.");
    } finally {
      setUploading(false);
    }
  };

  // 3. Function to handle sending chat questions
  const handleSend = async (e) => {
    e.preventDefault();
    if (!input.trim() || loading) return;

    const userQuery = input;
    setInput("");

    // Add user message to state
    setMessages((prev) => [...prev, { role: "user", text: userQuery }]);
    setLoading(true);

    try {
      // Call app.js -> FastAPI backend
      const response = await askQuestion(userQuery);

      // Add Bot response to state
      setMessages((prev) => [...prev, { role: "bot", text: response.answer }]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { role: "bot", text: "Error connecting to backend." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  // --- MODERN STYLE DEFINITIONS ---
  const colors = {
    bg: "#121212", // Deep Black/Dark Gray background
    paper: "#1e1e1e", // Slightly lighter gray for "paper" elements
    accent: "#00bcd4", // Cool Cyan for primary actions/user bubble
    textMain: "#ffffff",
    textSecondary: "#aaaaaa",
    botMsg: "#2d2d2d", // Mid-gray for bot bubble
  };

  return (
    <div
      style={{
        padding: "2rem",
        maxWidth: "900px", // Increased width for better reading
        margin: "0 auto",
        fontFamily: "'Segoe UI', Roboto, Helvetica, Arial, sans-serif",
        backgroundColor: colors.bg,
        color: colors.textMain,
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        gap: "2rem",
      }}
    >
      <header style={{ textAlign: "center", marginBottom: "1rem" }}>
        <h1
          style={{
            fontWeight: 800,
            fontSize: "2.5rem",
            margin: 0,
            lineHeight: 1.2,
          }}
        >
          RAG Knowledge <span style={{ color: colors.accent }}>Assistant</span>
        </h1>
        <p style={{ color: colors.textSecondary, marginTop: "0.5rem" }}>
          Chat with your PDFs using Retrieval-Augmented Generation.
        </p>
      </header>

      {/* Modern PDF Upload Section */}
      <section
        style={{
          padding: "1.5rem",
          backgroundColor: colors.paper,
          border: "1px solid #333", // Solid, subtle gray
          borderRadius: "12px",
          boxShadow: "0 4px 6px rgba(0,0,0,0.3)",
        }}
      >
        <h3
          style={{ marginTop: 0, marginBottom: "1rem", color: colors.textMain }}
        >
          <span style={{ fontSize: "1.3rem", marginRight: "0.5rem" }}>📂</span>
          Upload Documents
        </h3>
        <input
          type="file"
          accept=".pdf"
          multiple
          onChange={handleFileUpload}
          disabled={uploading}
          style={{
            color: colors.textSecondary,
            padding: "0.5rem",
            backgroundColor: "#2a2a2a",
            borderRadius: "6px",
            width: "100%",
            boxSizing: "border-box",
            cursor: uploading ? "not-allowed" : "pointer",
          }}
        />
        {uploading && (
          <p
            style={{
              color: colors.accent,
              fontWeight: "500",
              marginTop: "1rem",
            }}
          >
            <span className="spinner">⏳</span> Uploading to ChromaDB...
          </p>
        )}
      </section>

      {/* Cool Chat Messages Box */}
      <section
        style={{
          flex: 1, // Takes remaining vertical space
          backgroundColor: colors.paper,
          border: "1px solid #333",
          padding: "1.5rem",
          minHeight: "450px", // Increased min height
          borderRadius: "12px",
          display: "flex",
          flexDirection: "column",
          gap: "1rem",
          overflowY: "auto", // Allows scrolling if chat gets long
          boxShadow: "0 4px 15px rgba(0,0,0,0.4)",
        }}
      >
        {messages.length === 0 && (
          <div
            style={{
              flex: 1,
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <p
              style={{
                color: colors.textSecondary,
                textAlign: "center",
                fontStyle: "italic",
              }}
            >
              Upload a PDF above to build your knowledge base,
              <br /> then ask the first question below!
            </p>
          </div>
        )}

        {/* Message Mapping (Modern Bubbles) */}
        {messages.map((msg, index) => (
          <div
            key={index}
            style={{
              display: "flex",
              justifyContent: msg.role === "user" ? "flex-end" : "flex-start",
              marginBottom: "0.5rem",
            }}
          >
            <div
              style={{
                maxWidth: "75%", // Prevents message bubbles from crossing the whole screen
                padding: "1rem 1.25rem",
                borderRadius:
                  msg.role === "user"
                    ? "16px 16px 2px 16px"
                    : "16px 16px 16px 2px",
                backgroundColor:
                  msg.role === "user" ? colors.accent : colors.botMsg,
                color: msg.role === "user" ? "#121212" : colors.textMain, // Contrast text for user bubble
                boxShadow: "0 2px 4px rgba(0,0,0,0.2)",
                lineHeight: "1.5",
              }}
            >
              <strong>
                {msg.role === "user" ? (
                  "You: "
                ) : (
                  <span style={{ color: colors.accent }}>Bot: </span>
                )}
              </strong>
              <span style={{ whiteSpace: "pre-wrap" }}>{msg.text}</span>
            </div>
          </div>
        ))}

        {/* Loading Indicator */}
        {loading && (
          <div style={{ display: "flex", justifyContent: "flex-start" }}>
            <div
              style={{
                maxWidth: "75%",
                padding: "1rem 1.25rem",
                borderRadius: "16px 16px 16px 2px",
                backgroundColor: colors.botMsg,
                color: colors.textSecondary,
              }}
            >
              <strong style={{ color: colors.accent }}>Bot: </strong>
              <em>Searching documents & thinking...</em>
            </div>
          </div>
        )}
      </section>

      {/* Sleek Text Input Form */}
      <form
        onSubmit={handleSend}
        style={{ display: "flex", gap: "0.75rem", marginBottom: "1rem" }}
      >
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask a question about your documents..."
          style={{
            flex: 1,
            padding: "1rem",
            backgroundColor: "#2a2a2a",
            color: colors.textMain,
            border: "1px solid #444",
            borderRadius: "8px",
            fontSize: "1rem",
            outline: "none",
            transition: "border-color 0.2s",
          }}
          // Focus effect (basic inline, real CSS is better but this works)
          onFocus={(e) => (e.target.style.borderColor = colors.accent)}
          onBlur={(e) => (e.target.style.borderColor = "#444")}
        />
        <button
          type="submit"
          style={{
            padding: "1rem 1.5rem",
            backgroundColor: colors.accent,
            color: "#121212",
            border: "none",
            borderRadius: "8px",
            fontWeight: "bold",
            cursor: "pointer",
            fontSize: "1rem",
            textTransform: "uppercase",
            letterSpacing: "1px",
            transition: "opacity 0.2s",
          }}
          onMouseOver={(e) => (e.target.style.opacity = "0.85")}
          onMouseOut={(e) => (e.target.style.opacity = "1")}
        >
          Send
        </button>
      </form>
    </div>
  );
}
