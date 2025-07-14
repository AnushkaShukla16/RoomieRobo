Overview
An AI-driven assistant designed to automate the division, assignment, and follow-up of household chores among roommates or cohabitants. Managing shared tasks in a household or hostel setting can often lead to inefficiencies, conflict, or confusion. This agent streamlines chore management with intelligent assignment, reminders, conflict resolution, and progress tracking using a MySQL backend and Google ADK.

The agent accesses pending tasks from a shared database and uses logic-based tools to assign chores equitably.

It sends personalized reminders and follows up on incomplete tasks.

It resolves potential conflicts and tracks long-term chore participation, providing summaries of contributions.

This agent reduces manual workload, encourages fairness, and improves roommate collaboration.

Agent Details
Feature	Description
Interaction Type	Conversational
Complexity	Easy to Moderate
Agent Type	Multi-Agent
Components	Tools: Assign, Reminder, Conflict, Summary, Progress
Vertical	Productivity / Home Management

Agent architecture
This diagram illustrates the internal design and component structure of the Chores Agent system.

<img src="chores-agent.svg" alt="Chores Agent Architecture" width="800"/>
Setup and Installation
1. Prerequisites
Python 3.9+

Poetry
For dependency management.
Install Poetry

bash
Copy
Edit
pip install poetry
Google Cloud CLI
Install GCloud SDK

MySQL server
Ensure a running MySQL server and valid credentials for connection.

2. Installation
bash
Copy
Edit
# Clone the repository
git clone https://github.com/your-username/chores-agent.git
cd chores-agent

# Install dependencies
poetry install
3. Configuration
Set up a .env file or export environment variables:

bash
Copy
Edit
# Required for Vertex AI compatibility
export GOOGLE_GENAI_USE_VERTEXAI=true
export GOOGLE_CLOUD_PROJECT=<your-project-id>
export GOOGLE_CLOUD_LOCATION=<your-location>
export GOOGLE_CLOUD_STORAGE_BUCKET=<your-bucket-name>

# Required for MySQL connection
export DB_HOST=localhost
export DB_USER=root
export DB_PASSWORD=yourpassword
export DB_NAME=chores_db
Authenticate GCloud:

bash
Copy
Edit
gcloud auth application-default login
gcloud auth application-default set-quota-project $GOOGLE_CLOUD_PROJECT
Running the Agent
Using adk CLI:
bash
Copy
Edit
adk run chores_agent
Using Web UI:
bash
Copy
Edit
adk web
Navigate to the provided URL, select chores_agent, and interact via the chatbot interface.

Sample requests:

pgsql
Copy
Edit
who has pending tasks?
remind everyone
assign remaining tasks
show me task summary
resolve conflict between Aman and Priya
Example Interaction
markdown
Copy
Edit
* user: who are you?

Hello! I’m your Chores Assistant.

I help manage and divide household chores among roommates. I can assign tasks based on pending status, send reminders, resolve conflicts, and track contributions over time. How can I assist you today?

* user: assign tasks

Sure! Here's the current list of unassigned tasks:
- Wash dishes
- Clean balcony
- Take out trash

Assigning based on recent contributions...
- Wash dishes → Aman
- Clean balcony → Priya
- Take out trash → Riya

Assignments complete.
Running Tests
bash
Copy
Edit
poetry install --with dev

# Run unit tests
python3 -m pytest tests

# Optional evaluation scripts (if implemented)
python3 -m pytest eval
Deployment
To deploy on Vertex AI Agent Engine:

bash
Copy
Edit
poetry install --with deployment
python3 deployment/deploy.py --create
Once deployed, test using:

bash
Copy
Edit
export USER_ID=test_user
python3 deployment/test_deployment.py --resource_id=${AGENT_ENGINE_ID} --user_id=${USER_ID}
To delete:

bash
Copy
Edit
python3 deployment/deploy.py --delete --resource_id=${AGENT_ENGINE_ID}
Customization Ideas
Role Weighting: Prioritize based on availability or past workload.

Smart Reminders: Add time-aware nudging (e.g., “before dinner”).

Web UI Dashboard: Visualize task history, contribution stats, and weekly summaries.

Voice Assistant Integration: Enable control via Google Assistant or Alexa.

Integration with calendars: Automatically schedule chores with reminders.

