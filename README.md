# AI-First CRM HCP Module

## 📌 Overview

AI-First CRM HCP Module is an AI-powered Customer Relationship Management system designed for pharmaceutical field representatives to efficiently manage Healthcare Professional (HCP) interactions.

The application provides two ways to log interactions:

* **Structured form-based entry**
* **Conversational AI assistant**

The AI assistant allows representatives to describe meetings naturally, and the system automatically extracts important interaction details such as doctor name, discussion topics, sentiment, outcomes, and follow-up dates.

The project uses **LangGraph as an AI agent framework** and **Groq LLM (Gemma2-9B-IT)** for intelligent interaction processing.

---

# 🚀 Features

## AI Interaction Management

- Automatically extract interaction details from natural language
- Populate CRM fields using AI
- Convert relative dates into actual dates
- Detect doctor sentiment and outcomes
- Identify HCP name, discussion topics, and products
- Capture shared materials and follow-up dates
- Generate structured interaction records automatically

## AI Assistant Capabilities

- Edit existing interactions using conversational commands
- Generate concise interaction summaries
- Suggest professional follow-up actions
- Display previous HCP interaction history
- Analyze HCP engagement and product interest
- Provide AI-based sales recommendations

## Application Features

- React frontend with Redux state management
- FastAPI backend
- LangGraph AI agent orchestration
- Groq LLM integration using Gemma2-9B-IT model
- MySQL database support
- REST API communication between frontend and backend
- Conversational chat interface for interaction logging
- Structured form-based interaction view
---

# 🛠️ Tech Stack

## Frontend

* React.js
* Redux Toolkit
* Axios
* CSS
* Google Inter Font

## Backend

* Python
* FastAPI
* LangGraph
* Groq API
* Gemma2-9B-IT Model
* SQLAlchemy
* MySQL

---

# 🤖 LangGraph AI Agent

The LangGraph agent acts as the central decision-making system.

It analyzes user messages and routes them to the appropriate AI tool based on intent.

Example:

```
User:
"Summarize this interaction"

↓

LangGraph Router

↓

Summary Tool

↓

AI Generated Summary
```

---

# 🔧 LangGraph Tools

## 1. Log Interaction Tool

Purpose:

Extract interaction details from natural language input.

Capabilities:

* Identify HCP name
* Extract meeting date and time
* Identify discussed products/topics
* Detect sentiment
* Capture materials shared
* Extract follow-up date

Example:

Input:

```
Today I met Dr Smith at 11:30 AM.
We discussed Product X for diabetes treatment.
The doctor agreed to try the product.
I shared brochures and samples.
```

Output:

```json
{
 "hcpName":"Dr Smith",
 "date":"2026-07-12",
 "time":"11:30",
 "topics":"Product X, diabetes treatment",
 "materials":"brochures, samples",
 "sentiment":"Positive",
 "outcomes":"Doctor agreed to try the product"
}
```

---

## 2. Edit Interaction Tool

Purpose:

Modify existing interaction information.

Features:

* Updates only requested fields
* Maintains existing information
* Supports date and time conversion

Example:

```
Change doctor name to Dr John
and update sentiment to negative
```

Output:

```json
{
 "hcpName":"Dr John",
 "sentiment":"Negative"
}
```

---

## 3. Summary Tool

Purpose:

Creates a concise summary of the HCP interaction.

Example:

```
Summarize this interaction
```

Output:

```
Dr John discussed Product X for diabetes treatment.
The doctor showed interest and received brochures and samples.
Follow-up scheduled for 19-07-2026.
```

---

## 4. Follow-up Suggestion Tool

Purpose:

Provides next-step recommendations.

Example:

```
Suggest follow up actions
```

Output:

* Schedule follow-up meeting
* Address doctor concerns
* Share additional materials
* Collect product feedback

---

## 5. History Tool

Purpose:

Displays previous HCP interactions.

Example:

```
Show interaction history
```

Output:

```
Interaction History for Dr John

• Previous visit recorded
• Interested in Product X
• Requested product samples
```

---

## 6. HCP Insight Tool

Purpose:

Analyzes doctor engagement and recommends sales actions.

Provides:

* Engagement level
* Product interest analysis
* Sentiment evaluation
* Recommended next action

Example:

```
Give insight about this doctor
```

Output:

```
• Doctor engagement level is high.
• Strong interest shown in Product X.
• Positive sentiment detected.
• Follow up after product trial feedback.
```

---

# 📂 Project Structure

```
ai-crm-hcp/

│
├── backend/
│
│   ├── app/
│   │
│   ├── agents/
│   │   └── langgraph_agent.py
│   │
│   ├── tools/
│   │   ├── log_tool.py
│   │   ├── edit_tool.py
│   │   ├── summary_tool.py
│   │   ├── followup_tool.py
│   │   ├── history_tool.py
│   │   └── hcp_insight_tool.py
│   │
│   ├── routes/
│   ├── services/
│   └── main.py
│
├── frontend/
│
│   ├── src/
│   │
│   ├── components/
│   │
│   ├── redux/
│   │
│   └── api/
│
├── README.md
└── .gitignore

```

---

# ⚙️ Installation & Setup

## Backend Setup

Clone the repository:

```bash
git clone https://github.com/Shantika123/ai-crm-hcp.git
```

Navigate to backend:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI server:

```bash
python -m uvicorn app.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

# Frontend Setup

Navigate to frontend:

```bash
cd frontend
```

Install packages:

```bash
npm install
```

Start application:

```bash
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

# 🗄️ Database

Database:

```
MySQL
```

The database stores:

* HCP details
* Interaction records
* Dates and follow-ups
* Sentiment information
* Interaction history

---

# 🔄 AI Workflow

```
User Input

     ↓

React Chat Interface

     ↓

FastAPI API

     ↓

LangGraph Agent

     ↓

Tool Selection

     ↓

Groq LLM Processing

     ↓

Response

     ↓

Redux State Update

     ↓

UI Display
```

---

# 🧪 Example Commands

## Log Interaction

```
Today I met Dr Smith at 11:30 AM.
We discussed Product X for diabetes treatment.
The doctor was positive and agreed to try the product.
I shared brochures and samples.
Follow up next Monday.
```

## Edit Interaction

```
Change doctor name to Dr John and update sentiment to negative
```

## Summary

```
Summarize this interaction
```

## Follow-up

```
Suggest follow up actions
```

## History

```
Show interaction history
```

## Insights

```
Give insight about this doctor
```

---

# 🔮 Future Enhancements

* User authentication
* Role-based access control
* Sales dashboards
* Analytics and reporting
* Calendar integration
* Voice-based interaction logging
* Multiple HCP management

---

# 👨‍💻 Author

**Shantika Subhash Naik**

Computer Science & Engineering

AI-First CRM HCP Module Assignment
