print("Ai Career Intelligence System")
print("Welcome!")

name=input("Enter your name:")
education=input("Enter your education:")

print("\njJanhaviStudent Profile")
print("Name:",name)
print("Education:",education)


skills=[]
n=int(input("How many skils do you have? "))

for i in range(n):
    skill=input("Enter skill: ")
    skills.append(skill)

print("\nYour Skills: ")

for skill in skills:
    print("-",skill)



job_title = "Data Scientist"

required_skills = [
    "Python",
    "SQL",
    "Pandas",
    "Machine Learning",
    "Power BI"
]

print("\nJob:", job_title)
print("Required Skills:")

for skill in required_skills:
    print("-", skill)

matched_skills = []

for skill in skills:
    if skill in required_skills:
        matched_skills.append(skill)

print("\nMatched Skills:")

for skill in matched_skills:
    print("✓", skill)

missing_skills = []

for skill in required_skills:
    if skill not in skills:
        missing_skills.append(skill)

print("\nMissing Skills:")

for skill in missing_skills:
    print("✗", skill)

match_percentage = (len(matched_skills) / len(required_skills)) * 100

print("\nJob Match:", match_percentage, "%")



def calculate_match(student_skills, required_skills):

    matched = []

    for skill in student_skills:
        if skill in required_skills:
            matched.append(skill)

    score = (len(matched) / len(required_skills)) * 100

    return matched, score



matched, score = calculate_match(
    skills,
    required_skills
)

print("Match Score:", score)



import pandas as pd
jobs = pd.read_csv("jobs.xlsx")

print(jobs)


