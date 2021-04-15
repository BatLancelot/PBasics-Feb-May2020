start_num = int(input())
end_num = int(input())
magic_num = int(input())

iteration_count = 0
flag = False

for x in range(start_num, end_num + 1):
    for y in range(start_num, end_num + 1):
        n = x + y
        iteration_count += 1
        if n == magic_num:
            flag = True
            print(f"Combination N:{iteration_count} ({x} + {y} = {n})")
            break
    if flag:
        break

if not flag:
    print(f"{iteration_count} combinations - neither equals {magic_num}")
