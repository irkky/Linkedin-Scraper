def normalize_list_to_rows(profile_rows):
    
    exp_rows = []
    edu_rows = []

    for profile in profile_rows:
        url = profile.get("url")
        name = profile.get("name")

        # Normalize experiences
        experiences = profile.get("experiences")
        if experiences:
            for item in experiences.split(" ||| "):
                cleaned = item.strip()
                if cleaned:
                    exp_rows.append({
                        "url": url,
                        "name": name,
                        "experience_text": cleaned
                    })

        # Normalize education
        education = profile.get("education")
        if education:
            for item in education.split(" ||| "):
                cleaned = item.strip()
                if cleaned:
                    edu_rows.append({
                        "url": url,
                        "name": name,
                        "education_text": cleaned
                    })

    return exp_rows, edu_rows
