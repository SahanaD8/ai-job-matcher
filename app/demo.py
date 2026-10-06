from parser import extract_text, clean_text
from resume_info import get_resume_summary
from jobs import load_jobs, filter_jobs

text = clean_text(extract_text("data/sample_resume.pdf"))
summary = get_resume_summary(text)
print("Resume summary:", summary)

jobs = load_jobs("data/jobs.csv")
matches = filter_jobs(jobs, summary["location"], summary["experience"])
print(matches[["title", "company", "location", "min_exp", "max_exp"]])