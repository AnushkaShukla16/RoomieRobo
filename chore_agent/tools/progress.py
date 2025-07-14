from chore_agent.db import get_connection

def progress_tool():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT assigned_to, COUNT(*) as completed_count
        FROM chores
        WHERE status = 'completed'
        GROUP BY assigned_to
    """)
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    if not results:
        return "No one has completed any chores yet."

    output = "Chore Progress:\n"
    for user, count in results:
        output += f"- {user}: {count} completed chore(s)\n"
    return output
