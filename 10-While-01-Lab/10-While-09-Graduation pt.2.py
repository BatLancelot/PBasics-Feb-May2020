






name = input()

counter = 0
grade_sum = 0
excluded = 0

while counter < 12:
    grade = float(input())
    counter += 1
    if grade < 4.00:
        excluded += 1
        if excluded == 2:
            break
        continue
    grade_sum += grade

average_score = grade_sum / counter
if counter == 12:
    print(f'{name} graduated. Average grade: {average_score:.2f}')
else:
    print(f'{name} has been excluded at {counter-1} grade')
