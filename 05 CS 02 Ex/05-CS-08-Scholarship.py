import math

income_lv = float(input())
average_grade = float(input())
min_salary = float(input())

value_social = math.floor(min_salary * 0.35)
value_score = math.floor(average_grade * 25)
social = 0
excellent_results = 0

if income_lv < min_salary and average_grade > 4.5:
    social = 1

if average_grade >= 5.5:
    excellent_results = 1

if social == 1 and excellent_results == 1:
    if value_social > value_score:
        print(f'You get a Social scholarship {value_social} BGN')
    elif value_social < value_score:
        print(f'You get a scholarship for excellent results {value_score} BGN')
    elif value_social == value_score:
        print(f'You get a scholarship for excellent results {value_score} BGN')
elif social == 1 and excellent_results != 1:
    print(f'You get a Social scholarship {value_social} BGN')
elif social != 1 and excellent_results == 1:
    print(f'You get a scholarship for excellent results {value_score} BGN')
else:
    print('You cannot get a scholarship!')
