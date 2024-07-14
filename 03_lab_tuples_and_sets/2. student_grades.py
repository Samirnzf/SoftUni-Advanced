number_of_students = int(input())

students = {}

for _ in range(number_of_students):
    data = tuple(input().split())
    name, grade = data[0], float(data[1])
    if name not in students:
        students[name] = []
    students[name].append(grade)

for student, grades in students.items():
    average_grade = sum(grades) / len(grades)
    print(f"{student} -> {' '.join([f'{g:.2f}' for g in grades])} (avg: {average_grade:.2f})")
