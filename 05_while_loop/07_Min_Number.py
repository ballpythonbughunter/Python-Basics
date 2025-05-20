# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя,
# намира най-малкото измежду тях и го принтира. Въвежда се по едно число на ред.

import sys

min_number = sys.maxsize

while True:
    data = input()
    if data == 'Stop':
        break

    current_number = int(data)

    if current_number < min_number:
        min_number = current_number

print(min_number)