# ============================================================
# 🎯 CUSTOMIZABLE DATA SECTION — EDIT NAMES HERE!
# ============================================================

# Realistic first and last names (expandable)
FIRST_NAMES = [
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda",
    "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica",
    "Thomas", "Sarah", "Charles", "Karen", "Emma", "Noah", "Olivia", "Liam", "Ava",
    "Mason", "Sophia", "Jacob", "Isabella", "Ethan", "Mia", "Lucas", "Charlotte",
    "Henry", "Amelia", "Alexander", "Harper", "Benjamin", "Evelyn", "Daniel", "Abigail"
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker"
]

# Real subject names — no numbers, no underscores!
SUBJECT_NAMES = [
    "Mathematics",
    "English Literature",
    "Biology",
    "Chemistry",
    "Physics",
    "History",
    "Geography",
    "Computer Science"
]

# Configuration
NUM_STUDENTS = 1000
RANDOM_SEED = 42
GRADE_MIN = 40
GRADE_MAX = 99
OUTPUT_FILE = "student_results.csv"

# ============================================================
# ⚙️ DATA GENERATION & ANALYSIS (no need to edit below)
# ============================================================

import pandas as pd
import numpy as np

np.random.seed(RANDOM_SEED)

# Generate unique full names (very low chance of collision with 40×30 = 1200 combos)
student_names = []
used_names = set()

for _ in range(NUM_STUDENTS):
    while True:
        first = np.random.choice(FIRST_NAMES)
        last = np.random.choice(LAST_NAMES)
        name = f"{first} {last}"
        if name not in used_names:
            used_names.add(name)
            student_names.append(name)
            break

# Use clean subject names
subjects = SUBJECT_NAMES

# Generate grades
grades = np.random.randint(GRADE_MIN, GRADE_MAX + 1, size=(NUM_STUDENTS, len(subjects)))
df = pd.DataFrame(grades, columns=subjects)
df.insert(0, "Name", student_names)

# Compute average and grade
df["Average"] = df[subjects].mean(axis=1).round(2)

def grade_class(avg):
    if avg >= 90: return "A+"
    if avg >= 80: return "A"
    if avg >= 70: return "B"
    if avg >= 60: return "C"
    if avg >= 50: return "D"
    return "F"

df["Grade"] = df["Average"].apply(grade_class)

# ==============================
# 📊 REPORTING
# ==============================

print("=== SAMPLE OF RAW DATA ===")
print(df.head(), "\n")

print("=== CLASS STATISTICS ===")
print("Total students:", len(df))
print("Overall average score:", df[subjects].values.mean().round(2))
print("Highest average:", df['Average'].max())
print("Lowest average:", df['Average'].min())
print("A+ students:", (df['Grade'] == "A+").sum(), "\n")

print("=== SUBJECT-WISE STATISTICS ===")
print(df[subjects].describe().round(2), "\n")

print("=== TOP 10 STUDENTS ===")
print(df.nlargest(10, "Average")[["Name", "Average", "Grade"]].to_string(index=False), "\n")

print("=== BOTTOM 10 STUDENTS ===")
print(df.nsmallest(10, "Average")[["Name", "Average", "Grade"]].to_string(index=False), "\n")

print("=== EXTRA ANALYSIS ===")
print("Subject with highest average:", df[subjects].mean().idxmax())
fail_counts = (df[subjects] < 50).sum()
print("Subject with most fails:", fail_counts.idxmax(), f"({fail_counts.max()} fails)")

df.to_csv(OUTPUT_FILE, index=False)
print(f"\n✅ Saved to '{OUTPUT_FILE}'")
print("\n=== DONE ===")
