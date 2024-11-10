categories = [
    {"id": 1, "name": "Good", "rank": 2},
    {"id": 2, "name": "Bad", "rank": 3},
    {"id": 3, "name": "Perfect", "rank": 1},
    {"id": 4, "name": "Terrible", "rank": 4}
]

preferences = [
        {"id": 1,
         "type": "secondary",
         "links": [1],
         "rank": -1,
         "category": -1,
         "factor": "low_temp",
         "min": 60,
         "max": 70},
        {"id": 2,
         "type": "primary",
         "links": [1],
         "rank": 1,
         "category": 3,
         "factor": "high_temp",
         "min": 75,
         "max": 80},
        {"id": 3,
         "type": "primary",
         "links": [],
         "rank": 2,
         "category": 1,
         "factor": "high_temp",
         "min": 70,
         "max": 90}
]

forecasts = [
    {"date": "11/10/2024 12:00:00 PM", "high_temp": 77, "low_temp": 65},
    {"date": "11/11/2024 12:00:00 AM", "high_temp": 72, "low_temp": 55}
]

ratings = []

for f in forecasts:
    for p in preferences:
        if p["type"] == "primary":
            rating_exists = False
            for r in ratings:
                if (r.get("factor") == p.get("factor") and r.get("category") is not None):
                    rating_exists = True
                    break
            if rating_exists:
                continue
            sec_pref_met = True
            for link in p["links"]:
                for p_sec in preferences:
                    if p_sec["id"] == link and not (p_sec["min"] <= f.get(p_sec["factor"]) <= p_sec["max"]):
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
        if c["id"] == r["category"]:
            catg_sum += c["rank"]
            break
avg_rank = round(catg_sum / len(ratings))
for c in categories:
    if c["rank"] == avg_rank:
        avg_catg = c["id"]
        break
ratings.append({
    "date": f["date"],
    "factor": "overall",
    "category": avg_catg
})

print(ratings)
