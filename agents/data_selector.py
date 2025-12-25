def select_data(intent, fitbit_data):
    daily = fitbit_data["daily_metrics"]

    if intent["intent"] == "sleep":
        return daily[-1]["sleep"]

    if intent["intent"] == "activity":
        return [
            {"date": d["date"], "steps": d["steps"]}
            for d in daily
        ]

    if intent["intent"] == "heart":
        return [
            {"date": d["date"], "resting_hr": d["resting_hr"]}
            for d in daily
        ]

    return None
