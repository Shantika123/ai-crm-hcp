import json
from datetime import datetime

from app.services.groq_service import ask_llm
from app.database import get_connection



def save_interaction(data):

    connection = get_connection()

    cursor = connection.cursor()


    query = """
    INSERT INTO interactions
    (
        hcp_name,
        date,
        time,
        interaction_type,
        topics,
        materials,
        sentiment,
        outcomes,
        follow_up
    )

    VALUES
    (
        %s,%s,%s,%s,%s,%s,%s,%s,%s
    )
    """


    values = (

        data.get("hcpName"),

        data.get("date"),

        data.get("time"),

        data.get("interactionType"),

        data.get("topics"),

        data.get("materials"),

        data.get("sentiment"),

        data.get("outcomes"),

        data.get("followUp")

    )


    cursor.execute(query, values)

    connection.commit()


    cursor.close()

    connection.close()




def log_interaction(message: str):


    today = datetime.now().strftime("%Y-%m-%d")


    prompt = f"""

You are an AI CRM assistant for pharmaceutical sales representatives.

Today's date:
{today}


Extract interaction details.

Return ONLY JSON.


Rules:

- Date format YYYY-MM-DD
- Time format HH:MM
- Sentiment: Positive, Negative or Neutral
- Materials only shared materials
- Outcomes describe meeting result


Return:

{{
"hcpName":"",
"date":"",
"time":"",
"interactionType":"",
"topics":"",
"materials":"",
"sentiment":"",
"outcomes":"",
"followUp":""
}}


User message:

{message}

"""


    response = ask_llm(prompt)


    response = (
        response
        .replace("```json","")
        .replace("```","")
        .strip()
    )


    try:

        data = json.loads(response)



        # Save into MySQL

        save_interaction(data)



        return data



    except Exception as e:

        return {

            "error":str(e),

            "raw":response

        }