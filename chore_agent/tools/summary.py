from chore_agent.db import get_connection

def summary_tool():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT assigned_to, task, status, assigned_date, completed_date
        FROM chores
        ORDER BY assigned_to
    """)
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    if not results:
        return "No chore data available."

    summary = "Chore Summary:\n"
    for row in results:
        person, task, status, assigned, completed = row
        summary += f"- {person}: {task} [{status}] (Assigned: {assigned}, Completed: {completed})\n"
    return summary
    