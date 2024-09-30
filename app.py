import os
import json
import streamlit as st
from crewai import Crew, Process
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from utils import scan_resumes
from agents import agents
from tasks import tasks

load_dotenv()

# Configuration
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Load the llm
llm = ChatGroq(
    model="groq/mixtral-8x7b-32768",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

# Load job requirements database
with open('job_requirements_db.json', 'r') as f:
    job_requirements_db = json.load(f)

st.title("AI Agent Candidate Screening")

# Sidebar for job requirements
st.sidebar.header("Company Job Requirements")
for job_title in job_requirements_db.keys():
    if st.sidebar.checkbox(job_title):
        st.sidebar.json(job_requirements_db[job_title])

# Main app
job_desire = st.text_input("Enter Job Title:")
resume_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if job_desire and resume_file:
    # Save uploaded file temporarily
    with open("temp_resume.pdf", "wb") as f:
        f.write(resume_file.getvalue())

    # Read resume content
    resume_content = scan_resumes("temp_resume.pdf")

    if st.button("Analyze Resume"):
        with st.spinner("Analyzing resume..."):
            # Creating agents and tasks
            job_requirements_researcher, resume_analyser = agents(llm)

            research, resume_swot_analysis = tasks(llm, job_desire, resume_content)

            # Building crew and kicking it off
            crew = Crew(
                agents=[job_requirements_researcher, resume_analyser],
                tasks=[research, resume_swot_analysis],
                verbose=1,
                process=Process.sequential
            )

            result = crew.kickoff()

            # Display results
            st.subheader("Analysis Results")
            st.json(result)

    # Clean up temporary file
    os.remove("temp_resume.pdf")

st.sidebar.markdown("---")
st.sidebar.text("HR Resume Analysis Tool")