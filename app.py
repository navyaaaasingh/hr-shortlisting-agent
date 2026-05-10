import os
import streamlit as st

from utils.document_parser import parse_resume
from agents.jd_parser_agent import parse_jd
from agents.profile_parser_agent import parse_candidate_profile
from agents.scoring_agent import score_candidate
from utils.report_generator import generate_dataframe

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.set_page_config(
    page_title="HR Shortlisting Agent",
    layout="wide"
)

st.title("AI HR Resume Shortlisting Agent")

jd_text = st.text_area("Paste Job Description")

uploaded_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

if st.button("Evaluate Candidates"):

    jd_data = parse_jd(jd_text)

    results = []

    for file in uploaded_files:

        path = os.path.join(UPLOAD_DIR, file.name)

        with open(path, "wb") as f:
            f.write(file.getbuffer())

        resume_text = parse_resume(path)

        candidate = parse_candidate_profile(resume_text)

        score = score_candidate(jd_data, candidate)

        result = {
            "name": candidate["name"],
            **score
        }

        results.append(result)

    df = generate_dataframe(results)

    st.dataframe(df)

    for r in results:
        st.subheader(r["name"])
        st.json(r)
