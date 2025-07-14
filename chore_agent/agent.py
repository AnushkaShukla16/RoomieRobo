from chore_agent import prompt
from google.adk.agents import LlmAgent


from chore_agent.tools.reminder import reminder_tool
from chore_agent.tools.summary import summary_tool
from chore_agent.tools.conflict import resolve_conflicts  
from chore_agent.tools.progress import progress_tool
from chore_agent.tools.assign import assign_task


MODEL = "gemini-2.5-pro-preview-05-06"

agent = LlmAgent(
    name="chore_management_agent",
    model=MODEL,
    description=(
        "Agent to manage household chores with tools for assignment, reminders, "
        "summaries, conflict resolution, and progress tracking."
    ),
    instruction=prompt.HOUSEHOLD_AGENT_PROMPT,
    tools=[
        reminder_tool,
        summary_tool, 
        progress_tool,
        resolve_conflicts,
        assign_task,
    ],
        
)

root_agent = agent

