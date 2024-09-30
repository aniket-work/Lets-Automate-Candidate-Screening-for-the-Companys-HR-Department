import json
from crewai import Agent
from langchain.tools import Tool

# Load the job requirements database
with open('job_requirements_db.json', 'r') as f:
    job_requirements_db = json.load(f)

# Load the AI agent guidelines
with open('ai_agent_guideline/guide.json', 'r') as f:
    agent_guidelines = json.load(f)['ai_agent_guideline']


def search_job_requirements(job_title):
    """
    Search the job requirements database for a given job title.
    """
    job_title = job_title.lower().replace(' ', '_')
    if job_title in job_requirements_db:
        return json.dumps(job_requirements_db[job_title], indent=2)
    else:
        return f"No information found for job title: {job_title}"


# Create a Tool object for the search_job_requirements function
job_search_tool = Tool(
    name="Job Requirements Search",
    func=search_job_requirements,
    description="Searches the job requirements database for information about a specific job title."
)


def agents(llm):
    job_requirements_researcher = Agent(
        role=agent_guidelines['job_requirements_researcher']['role'],
        goal=agent_guidelines['job_requirements_researcher']['goal'],
        backstory=agent_guidelines['job_requirements_researcher']['backstory'],
        tools=[job_search_tool],  # Use the Tool object here
        verbose=agent_guidelines['job_requirements_researcher']['verbose'],
        llm=llm,
        max_iters=agent_guidelines['job_requirements_researcher']['max_iters']
    )

    resume_analyser = Agent(
        role=agent_guidelines['resume_analyser']['role'],
        goal=agent_guidelines['resume_analyser']['goal'],
        backstory=agent_guidelines['resume_analyser']['backstory'],
        verbose=agent_guidelines['resume_analyser']['verbose'],
        llm=llm,
        max_iters=agent_guidelines['resume_analyser']['max_iters'],
        allow_delegation=agent_guidelines['resume_analyser']['allow_delegation']
    )
    return job_requirements_researcher, resume_analyser