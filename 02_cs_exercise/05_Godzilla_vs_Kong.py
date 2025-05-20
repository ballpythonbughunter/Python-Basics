# Декорът за филма е на стойност 10% от бюджета.
# · При повече от 150 статиста, има отстъпка за облеклото на стойност 10%.

# Ред 1. Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# Ред 2. Брой на статистите – цяло число в интервала [1 … 500]
# Ред 3. Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]

# Ако парите за декора и дрехите са повече от бюджета:
# o "Not enough money!"
# o "Wingard needs {парите недостигащи за филма} leva more."
# · Ако парите за декора и дрехите са по малко или равни на бюджета:
# o "Action!"
# o "Wingard starts filming with {останалите пари} leva left."

budget = float(input())
statists = int(input())
clothes = float(input())

decoration = budget * 0.1
clothes_total = statists * clothes

if statists > 150:
    clothes_total -= clothes_total * 0.1

if (decoration + clothes_total) > budget:
    missing_amount = (clothes_total + decoration) - budget
    print('Not enough money!')
    print(f"Wingard needs {missing_amount:.2f} leva more.")

else:
    # (decoration + clothes_total) <= budget:
    left_amount = budget - (clothes_total + decoration)
    print("Action!")
    print(f"Wingard starts filming with {left_amount:.2f} leva left.")