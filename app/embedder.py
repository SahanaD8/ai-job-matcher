from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

resume = "I know Python and SQL and have worked on data projects"
job_a = "Looking for a Python developer to clean and analyse data"
job_b = "Hiring a chef for a busy restaurant kitchen"

embeddings = model.encode([resume, job_a, job_b])

print("Resume vs job A:", util.cos_sim(embeddings[0], embeddings[1]).item())
print("Resume vs job B:", util.cos_sim(embeddings[0], embeddings[2]).item())