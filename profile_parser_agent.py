import json
import re

from utils.groq_client import ask_groq

def extract_json(text):

    match = re.search(r'\{.*\}', text, re.DOTALL)

    if match:
        return match.group()

    return "{}"

def parse_candidate_profile(resume_text):

    prompt = f"""
    Extract structured candidate information.

    Return ONLY JSON.

    {{
        "name": "",
        "skills": [],
        "experience": "",
        "education": "",
        "projects": [],
        "certifications": [],
        "communication_quality": ""
    }}

    Resume:
    {resume_text}
    """

    response = ask_groq(prompt)

    try:

        cleaned = extract_json(response)

        return json.loads(cleaned)

    except Exception as e:

        print("Groq Response:", response)

        return {
            "name": "Unknown",
            "skills": [],
            "experience": "",
            "education": "",
            "projects": [],
            "certifications": [],
            "communication_quality": ""
        }