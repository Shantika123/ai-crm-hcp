import json
import re

from app.services.groq_service import ask_llm
from app.database import get_connection



# ---------------- UPDATE MYSQL ----------------

def update_interaction_database(updated_data):

    connection = get_connection()

    cursor = connection.cursor()


    fields = []
    values = []


    mapping = {
        "hcpName": "hcp_name",
        "date": "date",
        "time": "time",
        "interactionType": "interaction_type",
        "topics": "topics",
        "materials": "materials",
        "sentiment": "sentiment",
        "outcomes": "outcomes",
        "followUp": "follow_up"
    }


    for key, value in updated_data.items():

        if key in mapping:

            fields.append(
                f"{mapping[key]} = %s"
            )

            values.append(value)



    if fields:

        query = f"""
        UPDATE interactions
        SET {", ".join(fields)}
        ORDER BY id DESC
        LIMIT 1
        """


        cursor.execute(
            query,
            tuple(values)
        )


        connection.commit()



    cursor.close()

    connection.close()




# ---------------- EDIT TOOL ----------------

def edit_interaction(current_data, instruction):


    prompt = f"""
You are an AI CRM Interaction Editor.

Current Interaction Data:

{json.dumps(current_data, indent=2)}


User Instruction:

{instruction}


Your job:

Update ONLY the fields mentioned by the user.


Supported Fields:

- hcpName
- date
- time
- interactionType
- topics
- materials
- sentiment
- outcomes
- followUp


Rules:

1. Keep unchanged fields untouched.
2. Return ONLY modified fields.
3. Time format must be HH:MM.
4. Dates must be YYYY-MM-DD.
5. Sentiment must be Positive, Negative or Neutral.
6. Return valid JSON only.
7. No markdown.
8. No explanations.


Examples:


User:
Change doctor name to Dr John and sentiment to negative.


Output:

{{
"hcpName":"Dr John",
"sentiment":"Negative"
}}


User:
Update meeting time to 3 PM.


Output:

{{
"time":"15:00"
}}


User:
Change follow up to Friday.


Output:

{{
"followUp":"2026-07-17"
}}

"""


    response = ask_llm(prompt)


    print("\n========== RAW EDIT RESPONSE ==========")
    print(response)
    print("=======================================\n")



    try:

        cleaned = re.sub(
            r"```json|```",
            "",
            response
        ).strip()


        updated_data = json.loads(cleaned)



        updated_data = {
            key:value
            for key,value in updated_data.items()
            if value not in ["", None, []]
        }



        # Save changes in MySQL

        update_interaction_database(
            updated_data
        )



        return updated_data



    except Exception as e:


        print(
            "EDIT TOOL ERROR:",
            e
        )


        return {
            "error":str(e),
            "raw":response
        }