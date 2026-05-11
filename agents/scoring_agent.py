from utils.embeddings import semantic_similarity

WEIGHTS = {
    "skills_match": 0.30,
    "experience_relevance": 0.25,
    "education_certs": 0.15,
    "projects_portfolio": 0.20,
    "communication_quality": 0.10
}


def calculate_dimension_score(value):

    if value >= 85:
        return 10

    elif value >= 50:
        return 5

    return 2


def convert_to_text(value):

    if isinstance(value, list):
        return " ".join([str(v) for v in value])

    elif isinstance(value, str):
        return value

    return ""


def score_candidate(jd, candidate):

    jd_skills = convert_to_text(
        jd.get("skills", [])
    )

    candidate_skills = convert_to_text(
        candidate.get("skills", [])
    )

    jd_projects = convert_to_text(
        jd.get("projects", [])
    )

    candidate_projects = convert_to_text(
        candidate.get("projects", [])
    )

    jd_experience = str(
        jd.get("experience", "")
    )

    candidate_experience = str(
        candidate.get("experience", "")
    )

    jd_education = str(
        jd.get("education", "")
    )

    candidate_education = str(
        candidate.get("education", "")
    )

    jd_communication = str(
        jd.get("communication_requirements", "")
    )

    candidate_communication = str(
        candidate.get("communication_quality", "")
    )

    skill_similarity = semantic_similarity(
        jd_skills,
        candidate_skills
    )

    project_similarity = semantic_similarity(
        jd_projects,
        candidate_projects
    )

    experience_similarity = semantic_similarity(
        jd_experience,
        candidate_experience
    )

    education_similarity = semantic_similarity(
        jd_education,
        candidate_education
    )

    communication_similarity = semantic_similarity(
        jd_communication,
        candidate_communication
    )

    scores = {
        "skills_match": calculate_dimension_score(
            skill_similarity
        ),

        "experience_relevance": calculate_dimension_score(
            experience_similarity
        ),

        "education_certs": calculate_dimension_score(
            education_similarity
        ),

        "projects_portfolio": calculate_dimension_score(
            project_similarity
        ),

        "communication_quality": calculate_dimension_score(
            communication_similarity
        )
    }

    total = (
        scores["skills_match"] * WEIGHTS["skills_match"] +
        scores["experience_relevance"] * WEIGHTS["experience_relevance"] +
        scores["education_certs"] * WEIGHTS["education_certs"] +
        scores["projects_portfolio"] * WEIGHTS["projects_portfolio"] +
        scores["communication_quality"] * WEIGHTS["communication_quality"]
    ) * 10

    recommendation = (
        "Hire"
        if total >= 75
        else "No Hire"
    )

    return {
        "scores": scores,
        "total_score": round(total, 2),
        "recommendation": recommendation
    }
