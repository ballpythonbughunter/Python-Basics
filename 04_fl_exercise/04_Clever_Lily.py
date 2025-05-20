# Лили вече е на N години. За всеки свой рожден ден тя получава подарък.
# · За нечетните рождени дни (1, 3, 5...n) получава играчки.
# · За четните рождени дни (2, 4, 6...n) получава пари.
#
# За втория рожден ден получава 10.00 лв, като сумата се увеличава с 10.00 лв., за всеки следващ четен рожден
# ден (2 -> 10, 4 -> 20, 6 -> 30...и т.н.). През годините Лили тайно е спестявала парите. Братът на Лили, в годините, които
# тя получава пари, взима по 1.00 лев от тях. Лили продала играчките получени през годините, всяка за P лева и добавила сумата
# към спестените пари. С парите искала да си купи пералня за X лева. Напишете програма, която да пресмята, колко пари е събрала и дали ѝ стигат да си купи пералня.


n = int(input())
wash_machine_price = float(input())
toy_price = int(input())

toy_counter = 0.00
savings_counter = 0.00
money_gifted = 10.00

for i in range(1, n + 1):
    if i % 2 == 0:
        savings_counter += money_gifted
        money_gifted += 10.00
        savings_counter -= 1.00
    else:
        toy_counter += 1.00

total_toy_savings = toy_price * toy_counter

if wash_machine_price <= (savings_counter + total_toy_savings):
    print(f'Yes! {((savings_counter + total_toy_savings) - wash_machine_price):.2f}')
else:
    print(f'No! {(abs((savings_counter + total_toy_savings) - wash_machine_price)):.2f}')