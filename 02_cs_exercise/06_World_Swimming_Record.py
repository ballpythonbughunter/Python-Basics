# 1. Рекордът в секунди – реално число;
# 2. Разстоянието в метри – реално число;
# 3. Времето в секунди, за което плува разстояние от 1 м. - реално число.

# съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди. Когато се изчислява колко пъти Иван ще се забави,
# в резултат на съпротивлението на водата, резултатът трябва да се закръгли надолу до най-близкото цяло число.
# Да се изчисли времето в секунди, за което Иван ще преплува разстоянието и разликата спрямо Световния рекорд.

# Ако Иван е подобрил Световния рекорд (времето му е по-малко от рекорда) отпечатваме:
# o " Yes, he succeeded! The new world record is {времето на Иван} seconds."
# · Ако НЕ е подобрил рекорда (времето му е по-голямо или равно на рекорда) отпечатваме:
# o "No, he failed! He was {недостигащите секунди} seconds slower."

record_time = float(input())
distance = float(input())
onemetertime_sec = float(input())

# time = distance * onemetertime_sec

from math import floor
delays = floor(distance // 15)

total_delay_time = delays * 12.5
total_time = distance * onemetertime_sec + total_delay_time

if total_time < record_time:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {(total_time - record_time):.2f} seconds slower.")

