# BOOK version

import math

volume = int(input())
pipe1 = int(input())
pipe2 = int(input())
hours = float(input())

water = (pipe1 + pipe2) * hours

if water <= volume:
    print('The pool is {0}% full. Pipe 1: {1}%. Pipe 2: {2}%.'.format(
        math.trunc(water / volume * 100),
        math.trunc(pipe1 * hours / water * 100),
        math.trunc(pipe2 * hours / water * 100)
    ))
else:
    print('For {0} hours the pool overflows with {1} liters.'.format(
        hours,
        water - volume
    ))

# My version

import math

volume = int(input())
pipe1 = int(input())
pipe2 = int(input())
hours = float(input())

water = (pipe1 + pipe2) * hours

volume_part = math.trunc(water / volume * 100)
pipe1_part = math.trunc(pipe1 * hours / water * 100)
pipe2_part = math.trunc(pipe2 * hours / water * 100)
overflow = water - volume

if water <= volume:
    print(f'The pool is {volume_part}% full. Pipe 1: {pipe1_part}%. Pipe 2: {pipe2_part}%.')
else:
    print(f'For {hours} hours the pool overflows with {overflow} liters.')
