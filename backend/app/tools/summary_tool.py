from datetime import datetime
from app.services.groq_service import ask_llm


def summarize_interaction(current_data):

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
You are an AI CRM assistant.

Current Interaction:

{data}


Rules:
- Mention doctor name.
- Mention products discussed.
- Mention sentiment.
- Mention materials shared.
- Mention follow-up date.
- Display follow-up date in DD-MM-YYYY format.
- Keep it under 5 lines.
- Return plain text only.
"""

    return ask_llm(prompt)