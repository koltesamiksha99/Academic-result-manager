print("=" * 30)
print("📚 ACADEMIC RESULT MANAGER 📚")
print("=" * 30)

name = input("Enter Student Name: ")
academic_class = input("Enter Academic Class: ")

subjects = int(input("Enter Number of Subjects: "))

subject_names = []
subject_marks = []

for i in range(subjects):
    subject = input(f"\nEnter Subject {i + 1} Name: ")

    while True:
        marks = int(input(f"Enter {subject} Marks (0-100): "))

        if marks >= 0 and marks <= 100:
            break
        else:
            print("Invalid Marks! Enter marks between 0 and 100.")

    subject_names.append(subject)
    subject_marks.append(marks)

total = sum(subject_marks)
maximum_marks = subjects * 100
percentage = (total / maximum_marks) * 100

highest_marks = max(subject_marks)
lowest_marks = min(subject_marks)

highest_index = subject_marks.index(highest_marks)
lowest_index = subject_marks.index(lowest_marks)

highest_subject = subject_names[highest_index]
lowest_subject = subject_names[lowest_index]

result = "PASS"
for mark in subject_marks:
    if mark < 35:
        result = "FAIL"
        break

if percentage >= 90:
    grade = "A+"
    result_class = "Outstanding"
elif percentage >= 80:
    grade = "A"
    result_class = "First Class with Distinction"
elif percentage >= 70:
    grade = "B"
    result_class = "First Class"
elif percentage >= 60:
    grade = "C"
    result_class = "Second Class"
elif percentage >= 50:
    grade = "D"
    result_class = "Pass Class"
elif percentage >= 35:
    grade = "E"
    result_class = "Pass Class"
else:
    grade = "F"
    result_class = "Fail"

print("\n" + "=" * 15)
print("ACADEMIC RESULT")
print("=" * 15)

print("Student Name :", name)
print("Academic Class :", academic_class)

print("\nSubject Wise Marks")
for i in range(subjects):
    print(subject_names[i], ":", subject_marks[i])

print("-" * 20)
print("Total Marks :", total, "/", maximum_marks)
print("Percentage :", round(percentage, 2), "%")
print("Grade :", grade)
print("Result Class :", result_class)
print("Result :", result)

print("Highest Subject :", highest_subject, "-", highest_marks)
print("Lowest Subject :", lowest_subject, "-", lowest_marks)

print("=" * 15)
print("Thank You!")
print("=" * 15)
