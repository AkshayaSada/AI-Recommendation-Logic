# Tech Stack Recommender

jobs = {
    "Data Scientist": [
        "python",
        "machine learning",
        "data analysis",
        "statistics",
        "sql"
    ],

    "Web Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "python"
    ],

    "DevOps Engineer": [
        "aws",
        "docker",
        "kubernetes",
        "linux",
        "git"
    ],

    "AI Engineer": [
        "python",
        "machine learning",
        "deep learning",
        "tensorflow",
        "data science"
    ]
}

print("=== TECH STACK RECOMMENDER ===")
print("Enter 3 skills separated by commas")

user_input = input("Skills: ")

user_skills = [
    skill.strip().lower()
    for skill in user_input.split(",")
]

scores = {}

for job, skills in jobs.items():
    match_count = 0
    for skill in user_skills:
        if skill in skills:
            match_count += 1
    scores[job] = match_count

sorted_jobs = sorted(
    scores.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nRecommended Career Paths:")

for job, score in sorted_jobs[:3]:
    print(f"{job}  | Match Score: {score}")