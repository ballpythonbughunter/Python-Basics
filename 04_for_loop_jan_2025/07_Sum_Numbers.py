# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя и ги сумира.
# · От първия ред на входа се въвежда броят числа n.
# · От следващите n реда се въвежда по едно цяло число.
# Програмата трябва да прочете числата, да ги сумира и да отпечата сумата им.

n = int(input())

sum_numbers = 0

for _ in range(n):
    current_number = int(input())
    sum_numbers += current_number

    print(sum_numbers)


# ALTERNATIVE SHORT SOLUTION:
#
# n = int(input())
# print(sum(int(input()) for _ in range(n)))
#
