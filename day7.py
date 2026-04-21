# Dataset
students = [
    {"Name": "Amit", "Math": 80, "Science": 70, "English": 85},
    {"Name": "Riya", "Math": 90, "Science": 88, "English": 92},
    {"Name": "John", "Math": 60, "Science": 65, "English": 70}
]

# 1. Average marks per student
for s in students:
    s["Average"] = (s["Math"] + s["Science"] + s["English"]) / 3

# 2. Find topper
topper = max(students, key=lambda x: x["Average"])["Name"]

# 3. Count students above overall average
overall_avg = sum(s["Average"] for s in students) / len(students)
above_avg_count = sum(1 for s in students if s["Average"] > overall_avg)

# BONUS: Grade column
def grade(avg):
    if avg >= 90: return "A+"
    elif avg >= 75: return "A"
    elif avg >= 60: return "B"
    else: return "C"

for s in students:
    s["Grade"] = grade(s["Average"])

# BONUS: Subject-wise average
subjects = ["Math", "Science", "English"]
subject_avg = {sub: sum(s[sub] for s in students)/len(students) for sub in subjects}

# Output
print("Student Dashboard:")
for s in students:
    print(s)

print("\nTopper:", topper)
print("Overall Average:", overall_avg)
print("Students Above Average:", above_avg_count)
print("\nSubject-wise Average:", subject_avg)

