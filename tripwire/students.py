students = [
    {"name": "hermione", "score": 95},
    {"name": "ron", "score": 62},
    {"name": "harry", "score": 78},
]

high_scores = [student["name"].upper() for student in students if student["score"] >= 70]
print(high_scores)