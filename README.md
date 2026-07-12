# AI-First CRM HCP Module

## Overview

This project is an AI-powered Customer Relationship Management (CRM) system for Healthcare Professional (HCP) interactions. It enables pharmaceutical sales representatives to log and manage doctor interactions using a conversational AI assistant instead of manually filling out forms.

The application uses LangGraph to orchestrate AI tools and Groq's Gemma2-9B-IT model to understand natural language, extract structured information, and assist field representatives.

---

## Features

* AI-driven interaction logging using natural language
* Automatic form population
* AI-based interaction editing
* AI-generated interaction summaries
* AI-generated follow-up suggestions
* HCP interaction history
* HCP engagement insights
* Redux state management
* FastAPI backend
* LangGraph agent orchestration
* MySQL database integration

---

## Tech Stack

### Frontend

* React
* Redux Toolkit
* Axios
* CSS
* Google Inter Font

### Backend

* Python
* FastAPI
* LangGraph
* Groq API (Gemma2-9B-IT)
* MySQL
* SQLAlchemy

---

## LangGraph Tools

### 1. Log Interaction Tool

* Extracts structured interaction data from natural language.
* Automatically fills the interaction form.
* Saves the interaction to the database.

### 2. Edit Interaction Tool

* Updates only the fields specified by the user.
* Preserves all other interaction details.

### 3. Summary Tool

* Generates a concise summary of the interaction.

### 4. Follow-up Tool

* Suggests professional follow-up actions based on the interaction.

### 5. History Tool

* Displays previous interactions for the selected HCP.

### 6. HCP Insight Tool

* Analyzes engagement level.
* Identifies product interest.
* Reviews interaction sentiment.
* Suggests the next sales action.

---

## Project Structure

```text
ai-crm-hcp/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── database/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   └── tools/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── redux/
│   │   └── api/
│   └── package.json
│
├── .gitignore
└── README.md
```

---

## Installation

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python -m uvicorn app.main:app --reload
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## Database

* MySQL
* Stores HCP interaction records
* Supports interaction history and updates

---

## AI Workflow

1. User enters a natural language interaction.
2. LangGraph routes the request to the appropriate tool.
3. Groq LLM extracts or analyzes the information.
4. FastAPI processes the response.
5. Redux updates the UI.
6. Interaction is stored or updated in MySQL.

---

## Example Prompts

### Log Interaction

```
Today I met Dr Smith at 11:30 AM.
We discussed Product X for diabetes treatment.
The doctor was positive and agreed to try the product.
I shared brochures and samples.
Follow up next Monday.
```

### Edit Interaction

```
Change the doctor name to Dr John and update sentiment to negative.
```

### Summary

```
Summarize this interaction
```

### Follow-up

```
Suggest follow up actions
```

### History

```
Show interaction history
```

### Insight

```
Give insight about this doctor
```

---

## Future Enhancements

* Authentication and user roles
* Dashboard with analytics
* Calendar integration
* Voice-based interaction logging
* Multi-HCP interaction management

---

## Author

**Shantika Subhash Naik**

Computer Science & Engineering Graduate

AI-First CRM HCP Module Assignment
