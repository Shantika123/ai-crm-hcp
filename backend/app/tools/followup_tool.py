from datetime import datetime
from app.services.groq_service import ask_llm


def suggest_followup(current_data):

    data = current_data.copy()

    if data.get("followUp"):
        try:
            data["followUp"] = datetime.strptime(
                data["followUp"],
                "%Y-%m-%d"
            ).strftime("%d-%m-%Y")

        except ValueError:
            pass


    prompt = f"""
You are an AI CRM assistant for pharmaceutical sales representatives.


Current Interaction:

{data}


Suggest appropriate follow-up actions.


Rules:
- Return ONLY 4 concise bullet points.
- Mention doctor's name.
- Display follow-up date in DD-MM-YYYY format.
- Do NOT write an email.
- Do NOT include greetings.
- Keep response professional.
"""


    return ask_llm(prompt)