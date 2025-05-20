# Тони и приятели много обичат да ходят за риба и са толкова запалени по риболова, че решават да отидат на риболов с кораб. Цената за наема на кораба зависи от сезона и броя рибари:
# В зависимост от сезона:· Цената за наем на кораба през пролетта е 3000 лв.;
# · Цената за наем на кораба през лятото и есента е 4200 лв.;
# · Цената за наем на кораба през зимата е 2600 лв.
# В зависимост от броя на групата има различна отстъпка:· Ако групата е до 6 човека включително - отстъпка от 10%;
# · Ако групата е от 7 до 11 човека включително - отстъпка от 15%;
# · Ако групата е от 12 нагоре - отстъпка от 25%.
# Рибарите ползват допълнително 5% отстъпка, ако са четен брой, освен ако не е есен - тогава нямат допълнителна отстъпка, която се начислява след като се приспадне отстъпката по горните критерии.
# Напишете програма, която да пресмята дали рибарите ще съберат достатъчно пари.
# #
# · Бюджет на групата - цяло число;
# · Сезон - текст: "Spring", "Summer", "Autumn" или "Winter";
# · Брой рибари - цяло число.
#
# · Ако бюджетът е достатъчен: # "Yes! You have {останалите пари} leva left."
# · Ако бюджетът НЕ Е достатъчен: # "Not enough money! You need {сумата, която не достига} leva." Сумите трябва да са форматирани с точност до два знака след десетичната запетая.

budget = int(input())
season = input()
number_fisherman = int(input())

rent_price = 0
discount = 0
extra_discount = 0

if season == 'Spring':
    rent_price = 3000
    if 1 <= number_fisherman <= 6:
        discount = 0.1
    elif 7 <= number_fisherman <= 11:
        discount = 0.15
    elif number_fisherman >= 12:
        discount = 0.25

elif season == 'Summer' or season == 'Autumn':
    rent_price = 4200
    if number_fisherman <= 6:
        discount = 0.1
    elif 7 <= number_fisherman <= 11:
        discount = 0.15
    elif number_fisherman >= 12:
        discount = 0.25

elif season == 'Winter':
    rent_price = 2600
    if 1 <= number_fisherman <= 6:
        discount = 0.1
    elif 7 <= number_fisherman <= 11:
        discount = 0.15
    elif number_fisherman >= 12:
        discount = 0.25

if number_fisherman % 2 == 0 and not season == 'Autumn':
    extra_discount = 0.05

final_price = rent_price * (1 - discount) * (1 - extra_discount)

if budget >= final_price:
    print(f"Yes! You have {budget - final_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {final_price - budget:.2f} leva.")