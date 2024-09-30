import os
from fpdf import FPDF
from faker import Faker

# Initialize Faker
fake = Faker()

# Ensure the data directory exists
os.makedirs('data', exist_ok=True)

def generate_resume(name, email, phone, job_title, skills, experience, education):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Personal Information
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=name, ln=1, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Email: {email}", ln=1, align='C')
    pdf.cell(200, 10, txt=f"Phone: {phone}", ln=1, align='C')
    pdf.cell(200, 10, txt=f"Address: {fake.address()}", ln=1, align='C')

    # Objective
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Objective", ln=1)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Seeking a challenging position as a {job_title} where I can utilize my skills and experience to contribute to the company's success.")

    # Skills
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Skills", ln=1)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, ", ".join(skills))

    # Work Experience
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Work Experience", ln=1)
    pdf.set_font("Arial", size=12)
    for job in experience:
        pdf.cell(200, 10, txt=f"{job['company']} - {job['title']}", ln=1)
        pdf.cell(200, 10, txt=f"{job['date']}", ln=1)
        for responsibility in job['responsibilities']:
            pdf.cell(200, 10, txt=f"- {responsibility}", ln=1)
        pdf.ln(5)

    # Education
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Education", ln=1)
    pdf.set_font("Arial", size=12)
    for edu in education:
        pdf.cell(200, 10, txt=f"{edu['degree']}", ln=1)
        pdf.cell(200, 10, txt=f"{edu['school']}, {edu['year']}", ln=1)
        pdf.ln(5)

    return pdf

# Define resume data
resumes = [
    {
        "name": "Alex Johnson",
        "email": "alex.johnson@email.com",
        "phone": "(555) 123-4567",
        "job_title": "Software Developer",
        "skills": ["Python", "JavaScript", "React", "Node.js", "SQL", "Git", "Agile methodologies"],
        "experience": [
            {
                "company": "Tech Solutions Inc.",
                "title": "Senior Software Developer",
                "date": "2018 - Present",
                "responsibilities": [
                    "Developed and maintained web applications using React and Node.js",
                    "Implemented RESTful APIs and integrated with various third-party services",
                    "Mentored junior developers and conducted code reviews"
                ]
            },
            {
                "company": "CodeCraft Systems",
                "title": "Software Developer",
                "date": "2015 - 2018",
                "responsibilities": [
                    "Worked on full-stack development using Python and Django",
                    "Optimized database queries and improved application performance",
                    "Collaborated with cross-functional teams to deliver projects on time"
                ]
            }
        ],
        "education": [
            {
                "degree": "Bachelor of Science in Computer Science",
                "school": "University of Technology",
                "year": "2015"
            }
        ]
    },
    {
        "name": "Emily Chen",
        "email": "emily.chen@email.com",
        "phone": "(555) 987-6543",
        "job_title": "Data Analyst",
        "skills": ["Python", "R", "SQL", "Tableau", "Machine Learning", "Statistical Analysis", "Data Visualization"],
        "experience": [
            {
                "company": "Data Insights Co.",
                "title": "Senior Data Analyst",
                "date": "2019 - Present",
                "responsibilities": [
                    "Conducted advanced statistical analyses to derive actionable insights",
                    "Created interactive dashboards using Tableau for executive reporting",
                    "Developed predictive models using machine learning techniques"
                ]
            },
            {
                "company": "Analytics Firm LLC",
                "title": "Data Analyst",
                "date": "2016 - 2019",
                "responsibilities": [
                    "Performed data cleaning and preprocessing on large datasets",
                    "Generated regular reports and presentations for stakeholders",
                    "Assisted in developing and maintaining the company's data warehouse"
                ]
            }
        ],
        "education": [
            {
                "degree": "Master of Science in Data Science",
                "school": "State University",
                "year": "2016"
            },
            {
                "degree": "Bachelor of Science in Statistics",
                "school": "National College",
                "year": "2014"
            }
        ]
    },
    {
        "name": "Michael Roberts",
        "email": "michael.roberts@email.com",
        "phone": "(555) 246-8135",
        "job_title": "Project Manager",
        "skills": ["Project Planning", "Agile & Scrum", "Risk Management", "Stakeholder Communication", "Budgeting", "MS Project", "JIRA"],
        "experience": [
            {
                "company": "Global Projects Inc.",
                "title": "Senior Project Manager",
                "date": "2017 - Present",
                "responsibilities": [
                    "Led cross-functional teams in delivering complex IT projects",
                    "Managed project budgets exceeding $5 million",
                    "Implemented Agile methodologies, improving project delivery times by 20%"
                ]
            },
            {
                "company": "Innovative Solutions Corp.",
                "title": "Project Manager",
                "date": "2014 - 2017",
                "responsibilities": [
                    "Coordinated multiple projects simultaneously, ensuring on-time delivery",
                    "Developed and maintained project plans, schedules, and risk registers",
                    "Facilitated effective communication between team members and stakeholders"
                ]
            }
        ],
        "education": [
            {
                "degree": "Master of Business Administration",
                "school": "Business School of Management",
                "year": "2014"
            },
            {
                "degree": "Bachelor of Science in Business Administration",
                "school": "State University",
                "year": "2010"
            }
        ]
    }
]

# Generate 3 resumes
for i, resume_data in enumerate(resumes, 1):
    resume = generate_resume(**resume_data)
    resume.output(f"data/resume_{i}.pdf")

print("3 resumes have been generated in the 'data' folder.")