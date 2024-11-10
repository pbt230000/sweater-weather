categories = [
    {"ctg_id": 1, "ctg_name": "Good", "ctg_rank": 2},
    {"ctg_id": 2, "ctg_name": "Bad", "ctg_rank": 3},
    {"ctg_id": 3, "ctg_name": "Perfect", "ctg_rank": 1},
    {"ctg_id": 4, "ctg_name": "Terrible", "ctg_rank": 4}
]

prefs = [
        {"pref_id": 1,
         "pref_type": "secondary",
         "pref_links": [1],
         "pref_rank": 1,
         "category": -1,
         "factor": "low_temp",
         "min": 60,
         "max": 70},
        {"pref_id": 2,
         "pref_type": "primary",
         "pref_links": [1],
         "pref_rank": 1,
         "category": 3,
         "factor": "high_temp",
         "min": 75,
         "max": 80},
        {"pref_id": 3,
         "pref_type": "primary",
         "pref_links": [2],
         "pref_rank": 1,
         "category": 1,
         "factor": "high_temp",
         "min": 70,
         "max": 90}
]

forecast = [
    {"date": "11/10/2024 12:00:00 PM", "high_temp": 77, "low_temp": 65},
    {"date": "11/11/2024 12:00:00 AM", "high_temp": 72, "low_temp": 55}
]

ratings = []

for f in forecast:
    for p in prefs:
        sec_pref_met = True
        rating_exists = False
        for r in ratings:
            if (r.get("factor") == p.get("factor") and r.get("category") is not None):
                rating_exists = True
                break
        if rating_exists:
            continue
        if p["pref_type"] == "primary":
            for link in p["pref_links"]:
                for p_sec in prefs:
                    if p_sec["pref_id"] == link and not (p_sec["min"] <= f.get(p_sec["factor"]) <= p_sec["max"]):
                        sec_pref_met = False
                        break
            if sec_pref_met and p["min"] <= f[p.get("factor")] <= p["max"]:
                ratings.append({
                    "date": f["date"],
                    "factor": p["factor"],
                    "category": p["category"]
                })
                break
avg_catg = None
catg_sum = 0
for r in ratings:
    for c in categories:
        if c["ctg_id"] == r["category"]:
            catg_sum += c["ctg_rank"]
            break
avg_rank = round(catg_sum / len(ratings))
for c in categories:
    if c["ctg_rank"] == avg_rank:
        avg_catg = c["ctg_id"]
        break
ratings.append({
    "date": f["date"],
    "factor": "overall",
    "category": avg_catg
})

print(ratings)
