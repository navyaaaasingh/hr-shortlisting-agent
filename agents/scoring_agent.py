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


def score_candidate(jd, candidate):

    jd_skills = jd.get("skills", [])
    candidate_skills = candidate.get("skills", [])

    jd_projects = jd.get("projects", [])
    candidate_projects = candidate.get("projects", [])

    if not isinstance(jd_skills, list):
        jd_skills = []

    if not isinstance(candidate_skills, list):
        candidate_skills = []

    if not isinstance(jd_projects, list):
        jd_projects = []

    if not isinstance(candidate_projects, list):
        candidate_projects = []

    skill_similarity = semantic_similarity(
        " ".join(jd_skills),
        " ".join(candidate_skills)
    )

    project_similarity = semantic_similarity(
        " ".join(jd_projects),
        " ".join(candidate_projects)
    )

    experience_similarity = semantic_similarity(
        str(jd.get("experience", "")),
        str(candidate.get("experience", ""))
    )

    education_similarity = semantic_similarity(
        str(jd.get("education", "")),
        str(candidate.get("education", ""))
    )

    communication_similarity = semantic_similarity(
        str(jd.get("communication_requirements", "")),
        str(candidate.get("communication_quality", ""))
    )

    scores = {
        "skills_match": calculate_dimension_score(skill_similarity),
        "experience_relevance": calculate_dimension_score(experience_similarity),
        "education_certs": calculate_dimension_score(education_similarity),
        "projects_portfolio": calculate_dimension_score(project_similarity),
        "communication_quality": calculate_dimension_score(communication_similarity)
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
