from chore_agent.db import get_connection

def assign_task(task: str, person: str) -> str:
    """
    Add a new chore to the database for a given person.
    """
    
    conn = get_connection()
    cursor = conn.cursor()

   
    sql = "INSERT INTO chores (task, assigned_to, status, assigned_date) VALUES (%s, %s, 'pending', CURDATE())"
    cursor.execute(sql, (task, person))

    conn.commit()
    cursor.close()
    conn.close()

    return f" '{task}' has been assigned to {person}."

