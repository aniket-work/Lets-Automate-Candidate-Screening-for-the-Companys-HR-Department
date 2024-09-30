from crewai import Task
from agents import agents, search_job_requirements


def tasks(llm, job_desire, resume_content):
    job_requirements_researcher, resume_analyser = agents(llm)

    research = Task(
        description=f'''For the job position: {job_desire}, thoroughly research and identify the current market requirements. Your report should include:
        1. A comprehensive list of required technical skills and proficiency levels
        2. Soft skills that are crucial for success in this role
        3. Typical projects or responsibilities associated with this position
        4. Required years of experience and any specific domain expertise
        5. Educational background and certifications that are commonly required or preferred
        6. Any industry-specific knowledge or trends that candidates should be aware of
        Use the search_job_requirements function to query our database and supplement with your knowledge of current industry standards.''',
        expected_output='A detailed, structured report covering all aspects of the job requirements, formatted for easy comparison with a candidate\'s resume.',
        agent=job_requirements_researcher
    )

    resume_analysis = Task(
        description=f'''Analyze the provided resume content: 

        {resume_content} 

        Compare it against the job requirements report from the job_requirements_researcher. Your analysis should include:

        1. Strengths: Skills, experiences, or qualifications that closely match or exceed the job requirements
        2. Weaknesses: Areas where the candidate's profile falls short of the job requirements
        3. Growth: Potential areas for growth or additional qualifications that could make the candidate more competitive
        4. Red Flags: Market trends or competing candidates that might challenge this candidate's application

        Additionally, provide:
        5. A detailed resume match percentage, breaking down how well the candidate matches each major requirement category (e.g., skills, experience, education)
        6. Specific suggestions for improving the resume to better match the job requirements
        7. Any red flags or standout positive aspects in the resume

        Format your output as a JSON report with the following structure:
        {{
            "candidate": "Name of candidate",
            "job_title": "{job_desire}",
            "strengths": ["Strength 1", "Strength 2", ...],
            "weaknesses": ["Weakness 1", "Weakness 2", ...],
            "growth": ["growth 1", "growth 2", ...],
            "red flags": ["red flag 1", "red flag 2", ...],
            "resume_match_percentage": {{
                "overall": 85,
                "skills": 90,
                "experience": 80,
                "education": 85
            }},
            "suggestions": ["Suggestion 1", "Suggestion 2", ...],
            "red_flags": ["Red Flag 1", "Red Flag 2", ...],
            "standout_positives": ["Positive Aspect 1", "Positive Aspect 2", ...]
        }}''',
        expected_output='A comprehensive JSON report detailing the SWOT analysis, match percentage, and suggestions for the candidate\'s resume.',
        agent=resume_analyser,
        output_file='resume-report/resume_review.json'
    )
    return research, resume_analysis