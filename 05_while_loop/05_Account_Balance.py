# Напишете програма, която пресмята колко общо пари има в сметката, след като направите определен брой вноски.
# На всеки ред ще получавате сумата, която трябва да внесете в сметката, до получаване на команда "NoMoreMoney ".
# При всяка получена сума на конзолата трябва да се извежда "Increase: " + сумата и тя да се прибавя в сметката.
# Ако получите число по-малко от 0 на конзолата трябва да се изведе "Invalid operation!" и програмата да приключи.
# Когато програмата приключи трябва да се принтира "Total: " + общата сума в сметката форматирана до втория знак след десетичната запетая.

# account_total = 0
#
# while True:
#     data = input()
#
#     if data == 'NoMoreMoney':
#         break
#
#     current_sum = float(data)
#
#     if current_sum >= 0:
#         account_total += current_sum
#         print(f'Increase: {current_sum}')
#     else:
#         print("Invalid operation!")
#         break
#
# print(f'Total: {account_total:.2f}')

total_amount = 0

while True:
    deposit_amount = input()

    if deposit_amount == "NoMoreMoney":
        break

    current_deposit = float(deposit_amount)

    if current_deposit >= 0:
        total_amount += current_deposit
        print(f"Increase: {current_deposit:.2f}")
    else:
        print("Invalid operation!")
        break

print(f"Total: {total_amount:.2f}")










# if data != 'NoMoreMoney':
#        print(f'Increase: {data}')
#
#    current_sum = float(data)
#    account_total += float(data)
#
#    if float(data) < 0:
#        print("Invalid operation!")
#        break
