from datetime import datetime
from app.services.groq_service import ask_llm


def generate_hcp_insight(current_data):

    data = current_data.copy()


    # Convert followUp date format
    if data.get("followUp"):

        try:
            data["followUp"] = datetime.strptime(
                data["followUp"],
                "%Y-%m-%d"
            ).strftime("%d-%m-%Y")

        except ValueError:
            pass



    prompt = f"""
You are an AI assistant for a pharmaceutical CRM system.

Analyze the following Healthcare Professional interaction data:

{data}


Generate useful sales insights.

Rules:
- Mention doctor's engagement level.
- Mention product interest.
- Mention sentiment.
- Suggest next sales action.
- Always display dates in DD-MM-YYYY format.
- Do not use YYYY-MM-DD format.
- Return only 4 concise bullet points.
- Keep the response professional.
- Do not include greetings.
"""

    response = ask_llm(prompt)

    return response