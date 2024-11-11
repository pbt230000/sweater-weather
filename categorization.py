categories = [
    {"id": "1", "name": "Good", "rank": 2},
    {"id": "2", "name": "Bad", "rank": 3},
    {"id": "3", "name": "Perfect", "rank": 1},
    {"id": "4", "name": "Terrible", "rank": 4}
    ]

primary_preferences = [
        {"id": "4",
         "type": "primary",
         "links": [],
         "rank": 2,
         "category": "1",
         "factor": "high_temp",
         "min": 70,
         "max": 90},
        {"id": "2",
         "type": "primary",
         "links": ["1"],
         "rank": 1,
         "category": "3",
         "factor": "high_temp",
         "min": 75,
         "max": 80}
        ]

secondary_preferences = [
    {"id": "1",
     "type": "secondary",
     "links": ["2"],
     "factor": "low_temp",
     "min": 60,
     "max": 70}
    ]

forecasts = [
    {"date": "11/10/2024 12:00:00 PM", "high_temp": 70, "low_temp": 65},
    {"date": "11/10/2024 12:00:00 AM", "high_temp": 80, "low_temp": 70},
    {"date": "11/08/2024 12:00:00 PM", "high_temp": 95, "low_temp": 70}
    ]

ratings = []
primary_preferences_ranked = sorted(primary_preferences, key=lambda x: x['rank'])

for f in forecasts:
    for p in primary_preferences_ranked:
        rating_exists = False
        for r in ratings:
            if r.get("date") == f.get("date") and r.get("factor") == p.get("factor") and r.get("category") is not None:
                rating_exists = True
                break
        if rating_exists:
            continue
        secondary_preferences_met = True
        for link in p["links"]:
            for sec_p in secondary_preferences:
                if sec_p["id"] == link and not (sec_p["min"] <= f.get(sec_p["factor"]) <= sec_p["max"]):
                    secondary_preferences_met = False
                    break
        if secondary_preferences_met and p["min"] <= f[p.get("factor")] <= p["max"]:
            print(p["category"])
            ratings.append({
                "date": f["date"],
                "factor": p["factor"],
                "category": p["category"]})
    category_sum = 0
    category_count = 0
    for r in ratings:
        for c in categories:
            if r.get("date") == f.get("date") and c["id"] == r["category"]:
                category_sum += c["rank"]
                category_count += 1
    overall_category = None
    if category_count > 0:
        average_rank = round(category_sum / category_count)
        for c in categories:
            if c["rank"] == average_rank:
                overall_category = c["id"]
                break
        ratings.append({
            "date": f["date"],
            "factor": "overall",
            "category": overall_category})

for r in ratings:
    print(r)
