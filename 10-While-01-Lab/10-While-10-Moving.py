free_space_width = int(input())
free_space_length = int(input())
free_space_height = int(input())

total_free_space = free_space_height * free_space_length * free_space_width
used_space = 0
boxes = input()

while total_free_space >= used_space:
    if boxes == 'Done':
        break
    num_of_boxes = int(boxes)
    used_space += num_of_boxes
    if total_free_space < used_space:
        break
    boxes = input()

free_space_left = total_free_space - used_space

if total_free_space >= used_space:
    print(f'{free_space_left} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(free_space_left)} Cubic meters more.')
