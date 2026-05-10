import json
import re

from utils.groq_client import ask_groq

def extract_json(text):

    match = re.search(r'\{.*\}', text, re.DOTALL)

    if match:
        return match.group()

    return "{}"

def parse_jd(jd_text):

    prompt = f"""
    Extract the following from this Job Description.

    Return ONLY JSON.

    {{
        "skills": [],
        "experience": "",
        "education": "",
        "projects": [],
        "communication_requirements": ""
    }}

    Job Description:
    {jd_text}
    """

    response = ask_groq(prompt)

    try:

        cleaned = extract_json(response)

        return json.loads(cleaned)

    except Exception as e:

        print("Groq Response:", response)

        return {
            "skills": [],
            "experience": "",
            "education": "",
            "projects": [],
            "communication_requirements": ""
        }