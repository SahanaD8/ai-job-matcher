import re
from skills import find_skills

CITY_ALIASES = {
    "bengaluru": "Bengaluru",
    "bangalore": "Bengaluru",
    "hyderabad": "Hyderabad",
    "pune": "Pune",
    "mysuru": "Mysuru",
    "mysore": "Mysuru",
    "hubballi": "Hubballi",
    "hubli": "Hubballi",
}

def find_location(text):
    best_city = None
    best_pos = None
    for alias, city in CITY_ALIASES.items():
        match = re.search(r"\b" + alias + r"\b", text, re.IGNORECASE)
        if match and (best_pos is None or match.start() < best_pos):
            best_pos = match.start()
            best_city = city
    return best_city

def find_experience(text):
    pattern = r"(\d+(?:\.\d+)?)\+?\s*(?:years?|yrs?)\s+(?:of\s+)?experience"
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return float(match.group(1))
    return 0

def get_resume_summary(text):
    return {
        "location": find_location(text),
        "experience": find_experience(text),
        "skills": find_skills(text),
    }

if __name__ == "__main__":
    from parser import extract_text, clean_text

    text = clean_text(extract_text("data/sample_resume.pdf"))
    summary = get_resume_summary(text)
    print(summary)