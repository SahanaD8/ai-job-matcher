from sentence_transformers import SentenceTransformer, util
from parser import extract_text, clean_text
from resume_info import get_section
from skills import find_skills
from jobs import load_jobs

model = SentenceTransformer("all-MiniLM-L6-v2")

text = clean_text(extract_text("data/sample_resume.pdf"))
jobs = load_jobs("data/jobs.csv")

job_texts = (
    jobs["title"] + ". "
    + jobs["skills"].str.replace(";", ", ") + ". "
    + jobs["description"]
).tolist()

skills_text = "Skills: " + ", ".join(find_skills(text))
projects_text = get_section(text, "PROJECTS")
resume_for_match = skills_text + "\n" + projects_text

tokens = model.tokenizer(resume_for_match)["input_ids"]
print("Match text has:", len(tokens), "tokens (limit 256)")

job_embs = model.encode(job_texts)
jobs["score_full"] = util.cos_sim(model.encode(text), job_embs)[0].tolist()
jobs["score"] = util.cos_sim(model.encode(resume_for_match), job_embs)[0].tolist()

ranked = jobs.sort_values("score", ascending=False)
print(ranked[["title", "score_full", "score"]])