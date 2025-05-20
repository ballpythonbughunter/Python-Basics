# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя и проверява дали сред тях съществува число, което е равно на сумата на всички останали.
# · Ако има такъв елемент печата "Yes" и на нов ред "Sum = " + неговата стойност
# · Ако няма такъв елемент печата "No" и на нов ред "Diff = " + разликата между най-големия елемент и сумата на останалите (по абсолютна стойност

# n = int(input())
#
# sum = 0
# max_number = 0
#
# for _ in range(n):
#     current_number = int(input())
#
#     if current_number > max_number:
#         max_number = current_number
#
#     sum += current_number
#
# sum -= max_number
#
# if max_number == sum:
#     print("Yes")
#     print(f"Sum = {sum}")
#
# else:
#     diff = abs(max_number - sum)
#     print('No')
#     print(f"Diff = {diff}")
#






n = int(input())

sum = 0
max_num = 0

for _ in range(n):
    current_num = int(input())

    if current_num > max_num:
        max_num = current_num

    sum += current_num

sum -= max_num

if sum == max_num:
    print('Yes')
    print(f'Sum = {sum}')

else:
    diff = abs(max_num - sum)
    print('No')
    print(f'Diff = {diff}')