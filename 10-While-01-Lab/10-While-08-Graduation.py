name = input()

counter = 0
grade_sum = 0

while counter < 12:
    grade = float(input())
    if grade < 4.00:
        continue
    counter += 1
    grade_sum += grade

average_score = grade_sum / counter

print(f'{name} graduated. Average grade: {average_score:.2f}')
