from app.database import get_connection



def get_history(current_data):

    doctor = current_data.get(
        "hcpName",
        "Unknown Doctor"
    )


    connection = get_connection()

    cursor = connection.cursor(dictionary=True)


    query = """
    SELECT
        hcp_name,
        date,
        time,
        interaction_type,
        topics,
        materials,
        sentiment,
        outcomes,
        follow_up
    FROM interactions
    WHERE hcp_name = %s
    ORDER BY id DESC
    """


    cursor.execute(
        query,
        (doctor,)
    )


    records = cursor.fetchall()


    cursor.close()

    connection.close()



    history = []


    for item in records:

        history.append(
            f"""
Visit Date: {item['date']}
Time: {item['time']}
Type: {item['interaction_type']}
Topics: {item['topics']}
Materials: {item['materials']}
Sentiment: {item['sentiment']}
Outcome: {item['outcomes']}
Follow-up: {item['follow_up']}
""".strip()
        )



    if not history:

        history.append(
            f"No previous interactions found for {doctor}."
        )



    return {

        "doctor": doctor,

        "history": history

    }