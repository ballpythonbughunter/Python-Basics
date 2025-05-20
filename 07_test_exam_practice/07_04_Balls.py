# В кутия имаме неопределен брой топки с различни цветове, които ни носят различен брой точки. Задачата
# ни е да извадим Х бр. топки, които ще бъдат въведени от конзолата, като се има в предвид, че всеки
# различен цвят влияе на точките ни по следния начин:
#  Ако топката е “red” точките ни се повишават с 5.
#  Ако топката е “orange” точките ни се повишават с 10.
#  Ако топката е “yellow” точките ни се повишават с 15.
#  Ако топката е “white” точките ни се повишават с 20.
#  Ако топката е “black” точките ни се делят на 2, като закръгляме към по-малкото цяло число.
# Ако топката е с какъвто и да е цвят, различен от по-горните, точките не се манипулират и програмата
# продължава да работи.
# Вход:
# 1. От конзолата се чете 1 цяло число N, което е броят на топките в диапазон (0-1000).
# 2. След това се четат N на брой цветове.

import math

number_balls = int(input())

number_points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_balls = 0
times_divided = 0

for _ in range(number_balls):
    ball_color = input()

    if ball_color == 'red':
        number_points += 5
        red_balls += 1
    elif ball_color == 'orange':
        number_points += 10
        orange_balls += 1
    elif ball_color == 'yellow':
        number_points += 15
        yellow_balls += 1
    elif ball_color == 'white':
        number_points += 20
        white_balls += 1
    elif ball_color == 'black':
        number_points = math.floor(number_points / 2)
        times_divided += 1
    else:
        other_balls += 1
        continue

print(f"Total points: {number_points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_balls}")
print(f"Divides from black balls: {times_divided}")


