num_failed_score = int(input())

failed_counter = 0
task_counter = 0
sum_score = 0
task_name = ''

while task_name != 'Enough':
    task_name = input()
    if task_name == 'Enough':
        average_score = sum_score / task_counter
        print(f'Average score: {average_score:.2f}')
        print(f'Number of problems: {task_counter}')
        print(f'Last problem: {last_problem_name}')
        break
    score = int(input())
    if score <= 4:
        failed_counter += 1
    if failed_counter == num_failed_score:
        print(f'You need a break, {failed_counter} poor grades.')
        break
    sum_score += score
    task_counter += 1
    last_problem_name = task_name
