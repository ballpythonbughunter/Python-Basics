# Катерачи от цяла България се събират на групи и набелязват следващите върхове за изкачване. Според размера на групата, катерачите ще изкачват различни върхове.
# · Група до 5 човека – изкачват Мусала
# · Група от 6 до 12 човека – изкачват Монблан
# · Група от 13 до 25 човека – изкачват Килиманджаро
# · Група от 26 до 40 човека – изкачват К2
# · Група от 41 или повече човека – изкачват Еверест
# Да се напише програма, която изчислява процента на катерачите изкачващи всеки връх.

number_groups = int(input())

all_climbers = 0
number_climbers_musala = 0
number_climbers_montblanc = 0
number_climbers_kilimanjaro = 0
number_climbers_K2 = 0
number_climbers_everest = 0

for _ in range(number_groups):
    number_climbers = int(input())
    all_climbers += number_climbers

    if number_climbers <= 5:
        number_climbers_musala += number_climbers

    elif 6 <= number_climbers <= 12:
        number_climbers_montblanc += number_climbers

    elif 13 <= number_climbers <= 25:
        number_climbers_kilimanjaro += number_climbers

    elif 26 <= number_climbers <= 40:
        number_climbers_K2 += number_climbers

    else:
        number_climbers_everest += number_climbers

percentage_musala = number_climbers_musala / all_climbers * 100
percentage_montblanc = number_climbers_montblanc / all_climbers * 100
percentage_kilimanjaro = number_climbers_kilimanjaro / all_climbers * 100
percentage_k2 = number_climbers_K2 / all_climbers * 100
percentage_everest = number_climbers_everest / all_climbers * 100

print(f'{percentage_musala:.2f}%')
print(f'{percentage_montblanc:.2f}%')
print(f'{percentage_kilimanjaro:.2f}%')
print(f'{percentage_k2:.2f}%')
print(f'{percentage_everest:.2f}%')


