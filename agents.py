import json
from crewai import Agent
from langchain.tools import Tool

# Load the job requirements database
with open('job_requirements_db.json', 'r') as f:
    job_requirements_db = json.load(f)


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
        role='Job Requirements Research Analyst',
        goal='Provide up-to-date analysis of industry job requirements for the specified position',
        backstory='An expert analyst with deep knowledge of various job roles and their requirements.',
        tools=[job_search_tool],  # Use the Tool object here
        verbose=True,
        llm=llm,
        max_iters=1
    )

    resume_analyser = Agent(
        role='Resume Analyser',
        goal='Perform a SWOT Analysis on the Resume based on the industry Job Requirements report from job_requirements_researcher and provide a json report.',
        backstory='An expert in hiring with a great understanding of resumes and job market trends',
        verbose=True,
        llm=llm,
        max_iters=1,
        allow_delegation=True
    )
    return job_requirements_researcher, resume_analyser