import pandas as pd
pd.set_option("display.width", 200)

def load_jobs(path):
    jobs = pd.read_csv(path)
    return jobs

def filter_by_location(jobs, location):
    mask = jobs["location"].str.lower() == location.lower()
    return jobs[mask]

def filter_by_experience(jobs, years):
    mask = (jobs["min_exp"] <= years) & (years <= jobs["max_exp"])
    return jobs[mask]

def filter_jobs(jobs, location, years):
    result = filter_by_location(jobs, location)
    result = filter_by_experience(result, years)
    return result

if __name__ == "__main__":
    jobs = load_jobs("data/jobs.csv")
    result = filter_jobs(jobs, "Bengaluru", 1)
    print(result[["title", "company", "location", "min_exp", "max_exp"]])