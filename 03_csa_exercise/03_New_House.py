# Марин и Нели си купуват къща недалеч от София. Нели толкова много обича цветята, че Ви убеждава да напишете програма,
# която да изчисли колко ще им струва, за да засадят определен брой цветя и дали наличният бюджет ще им е достатъчен. Различните цветя са с различни цени:
# цвете              Роза Далия Лале Нарцис Гладиола
# Цена на брой в лева 5    3.80 2.80   3      2.50
# Съществуват следните отстъпки:
# · Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# · Ако Нели купи повече от 90 Далии - 15% отстъпка от крайната цена;
# · Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# · Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# · Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.
# От конзолата се четат 3 реда:
# · Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# · Брой цветя - цяло число;
# · Бюджет - цяло число.
# Да се отпечата на конзолата на един ред:
# · Ако бюджетът им е достатъчен - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
# · Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".
# Сумата да бъде форматирана до втория знак след десетичната запетая.

type_flowers = input()
number_flowers = int(input())
budget = float(input())

flower_price = 0
discount = 0

if type_flowers == 'Roses':
    flower_price = 5.00
    if number_flowers > 80:
        discount = 0.10
elif type_flowers == 'Dahlias':
    flower_price = 3.80
    if number_flowers > 90:
        discount = 0.15
elif type_flowers == 'Tulips':
    flower_price = 2.80
    if number_flowers > 80:
        discount = 0.15
elif type_flowers == 'Narcissus':
    flower_price = 3.00
    if number_flowers < 120:
        discount = -0.15
elif type_flowers == 'Gladiolus':
    flower_price = 2.50
    if number_flowers < 80:
        discount = -0.20


total_price = number_flowers * flower_price
total_discounted_price = total_price * (1 - discount)

if budget >= total_discounted_price:
    print(f"Hey, you have a great garden with {number_flowers} {type_flowers} and {(budget - total_discounted_price):.2f} leva left.")
else:
    print(f"Not enough money, you need {(total_discounted_price - budget):.2f} leva more.")






# if type_flowers == 'Roses' and number_flowers > 80:
#     flower_price = 5
#     final_price -= final_price * 0.9
# elif type_flowers == 'Roses' and number_flowers <= 80:
#     flower_price = 5
# elif type_flowers == 'Dahlias' and number_flowers > 90:
#     final_price -= final_price * 0.85
# elif type_flowers == 'Tulips' and number_flowers > 80:
#     final_price -= final_price * 0.85
# elif type_flowers == 'Narcissus' and number_flowers > 120:
#     final_price -= final_price * 1.15
# elif type_flowers == 'Gladiolus' and number_flowers > 80:
#     final_price -= final_price * 1.2
