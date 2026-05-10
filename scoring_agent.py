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

    skill_similarity = semantic_similarity(
        " ".join(jd["skills"]),
        " ".join(candidate["skills"])
    )

    project_similarity = semantic_similarity(
        " ".join(jd["projects"]),
        " ".join(candidate["projects"])
    )

    experience_similarity = semantic_similarity(
        jd["experience"],
        candidate["experience"]
    )

    education_similarity = semantic_similarity(
        jd["education"],
        candidate["education"]
    )

    communication_similarity = semantic_similarity(
        jd["communication_requirements"],
        candidate["communication_quality"]
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
