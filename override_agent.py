def apply_override(candidate, new_score, reason):

    candidate["override"] = {
        "updated_score": new_score,
        "reason": reason
    }

    candidate["total_score"] = new_score

    return candidate
