# Напишете програма, която чете n на брой цели числа. Принтирайте най-голямото и най-малкото число сред въведените.
# import sys

n = int(input())

max_number = -sys.maxsize
min_number = sys.maxsize

for _ in range(n):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number

    if current_number < min_number:
        min_number = current_number

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')


# ALTERNATIVE SOLUTION:
#
#
# n = int(input())
#
# numbers = [int(input()) for _ in range(n)]
# max_number = max(numbers)
# min_number = min(numbers)
#
# print(f'Max number: {max_number}')
# print(f'Min number: {min_number}')


