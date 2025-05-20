# Петър иска да купи N видеокарти, M процесора и P на брой рам памет. Ако броя на видеокартите е по-голям от този на
# процесорите получава 15% отстъпка от крайната сметка. Важат следните цени:
# · Видеокарта – 250 лв./бр.
# · Процесор – 35% от цената на закупените видеокарти/бр.
# · Рам памет – 10% от цената на закупените видеокарти/бр.
# Да се изчисли нужната сума за закупуване на материалите и да се пресметне дали бюджета ще му стигне.
#
# 1. Бюджетът на Петър - реално число в интервала [1.0…100000.0]
# 2. Броят видеокарти - цяло число в интервала [1…100]
# 3. Броят процесори - цяло число в интервала [1…100]
# 4. Броят рам памет - цяло число в интервала [1…100]
#
# · Ако бюджета е достатъчен:
# "You have {остатъчен бюджет} leva left!"
# · Ако сумата надхвърля бюджета:
# "Not enough money! You need {нужна сума} leva more!"

budget = float(input())
number_videocards = int(input())
number_processors = int(input())
number_ram = int(input())

total_price = number_videocards * 250 + number_processors * (number_videocards * 250 * 0.35) + number_ram * (number_videocards * 250 * 0.10)

if number_videocards > number_processors:
    total_price -= total_price * 0.15

if budget >= total_price:
    print(f"You have {(budget - total_price):.2f} leva left!")

else:
    print(f"Not enough money! You need {(total_price - budget):.2f} leva more!")



