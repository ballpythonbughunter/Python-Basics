# Задача 5. Грижи за кученце
# Ани намира кученце, за което ще се грижи, докато се намери някой да го осинови. То изяжда дневно
# определено количество храна. Да се напише програма, която проверява дали количеството храна, което е
# закупено за кученцето, ще е достатъчно докато кученцето бъде осиновено.
# От конзолата се прочитат:
# • Закупеното количество храна за кученцето в килограми – цяло число в интервала [1 …100]
# • На всеки следващ ред до получаване на команда Adopted ще получавате колко грама изяжда
# кученцето на всяко хранене - цяло число в интервала [10 …1000]

# WHILE LOOP

# bought_food = int(input())
# bought_food_grams = bought_food * 1000
# grams_per_feeding = 0
#
# for _ in '':
#     grams_per_feeding = int(input())
#     if '' == 'Adopted':
#         break
#     else:
#         bought_food_grams -= grams_per_feeding
#
#     if grams_per_feeding < 0:
#         print(f"Food is not enough. You need {abs(bought_food_grams - grams_per_feeding)} grams more.")
#     else:
#         print(f"Food is enough! Leftovers: {bought_food_grams - grams_per_feeding} grams.")
#

bought_food = int(input())
bought_food_grams = bought_food * 1000
total_eaten = 0

while True:
    command = input()
    if command == "Adopted":
        break

    grams_per_feeding = int(command)
    total_eaten += grams_per_feeding
if total_eaten <= bought_food_grams:
    print(f"Food is enough! Leftovers: {bought_food_grams - total_eaten} grams.")
else:
    print(f"Food is not enough. You need {total_eaten - bought_food_grams} grams more." )