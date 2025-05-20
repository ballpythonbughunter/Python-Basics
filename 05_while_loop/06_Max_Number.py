# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя,
# намира най-голямото измежду тях и го принтира. Въвежда се по едно число на ред.

import sys

max_number = -sys.maxsize

while True:
    data = input()
    if data == 'Stop':
        break

    current_number = int(data)

    if current_number > max_number:
        max_number = current_number

print(max_number)

