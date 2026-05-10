import pandas as pd

def generate_dataframe(results):

    rows = []

    for r in results:

        rows.append({
            "Candidate": r["name"],
            "Total Score": r["total_score"],
            "Recommendation": r["recommendation"]
        })

    df = pd.DataFrame(rows)

    return df.sort_values(
        by="Total Score",
        ascending=False
    )
