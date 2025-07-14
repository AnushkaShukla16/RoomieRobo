from chore_agent.db import get_connection

def get_pending_chores() -> str:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT task, assigned_to FROM chores WHERE status = 'pending'")
    chores = cursor.fetchall()
    cursor.close()
    conn.close()
    return chores

def reminder_tool() -> str:
    chores = get_pending_chores()
    if not chores:
        return "Everyone is up to date with their chores. Great job!"
    output = "Pending chores:\n"
    for task, person in chores:
        output += f"- {person} needs to complete: {task}\n"
    return output