# Calculate the average score
# Find the highest score
# Find the student with the highest score
# Find students with a score of 17 or higher
# Find students who passed the course (score >= 10)
students = {
    "Ali": 18,
    "Sara": 15,
    "Reza": 20,
    "Mina": 12,
    "Amir": 17
}

# Calculate the average score
total = 0

for score in students.values():
    total += score

average = total / len(students)

print("Average =", average)

# Find the highest score
for score in students.values():
    max_score = score
    break

for score in students.values():
    if score > max_score:
        max_score = score

print("Highest Score =", max_score)

# Find the student with the highest score
for student_name, score in students.items():
    if score == max_score:
        print("Top Student =", student_name)

# Find students with a score of 17 or higher
top_students = []

for student_name, score in students.items():
    if score >= 17:
        top_students.append(student_name)

print("Top Students =", top_students)

# Find students who passed the course
passed_students = []

for student_name, score in students.items():
    if score >= 10:
        passed_students.append(student_name)

print("Passed Students =", passed_students)
