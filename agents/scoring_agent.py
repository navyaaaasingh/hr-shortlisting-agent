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
        "projects
