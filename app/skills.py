import re

SKILLS = [
    "Python", "Java", "C", "C++", "JavaScript", "SQL", "MySQL", "MongoDB",
    "HTML", "CSS", "React.js", "Node.js", "Git", "REST API",
    "DSA", "OOP", "DBMS", "Machine Learning", "Data Science",
]


def find_skills(text):
    found = []
    for skill in SKILLS:
        pattern = r"(?<![A-Za-z0-9+#])" + re.escape(skill) + r"(?![A-Za-z0-9+#])"
        if re.search(pattern, text, re.IGNORECASE):
            found.append(skill)
    return found


if __name__ == "__main__":
    from parser import extract_text, clean_text

    text = clean_text(extract_text("data/sample_resume.pdf"))
    print(find_skills(text))
    