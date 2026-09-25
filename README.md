# ⚖️ LegalEase – AI-Powered Legal Document Generator

LegalEase is an AI-powered web application that helps users generate customizable legal document drafts using Generative AI.

## 📌 Project Overview

LegalEase allows users to enter document details such as document type, parties, effective date, and terms and conditions.

The application sends these details to a FastAPI backend, which uses Google Gemini AI to generate a structured legal document draft.

Users can then edit, preview, and download the generated document.

## ✨ Features

- 🤖 AI-powered legal document generation
- 📄 Multiple document types
- ✏️ Editable generated document
- 👀 Document preview
- 📥 Download as TXT
- 📝 Download as DOCX
- 📕 Download as PDF
- ⚡ FastAPI backend
- 🎨 Streamlit frontend
- 🔐 Environment-based Gemini API configuration
- ⚠️ Legal review disclaimer

## 📑 Supported Document Types

- Employment Contract
- Lease Agreement
- Non-Disclosure Agreement (NDA)
- Service Agreement
- Partnership Agreement
- Other

## 🛠️ Technologies Used

### Frontend
- Streamlit

### Backend
- FastAPI
- Uvicorn
- Pydantic

### AI
- Google Gemini API
- `google-genai`

### Document Processing
- python-docx
- fpdf2
- Pillow

### Programming Language
- Python

## 📂 Project Structure

```text
LegalEaseAI/
│
├── backend/
│   ├── ai_core/
│   │   ├── __init__.py
│   │   └── gemini_generator.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── document_formatter.py
│   │
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── routes.py
│
├── frontend/
│   └── app.py
│
├── tests/
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md