# В една кинозала столовете са наредени в правоъгълна форма в r реда и c колони. Има три вида прожекции с билети на различни цени:
# · Premiere - премиерна прожекция, на цена 12.00 лева;
# · Normal - стандартна прожекция, на цена 7.50 лева;
# · Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.
# Напишете програма, която чете тип прожекция (текст), брой редове и брой колони в залата (цели числа), въведени от
# потребителя, и изчислява общите приходи от билети при пълна зала. Резултатът да се отпечата във формат 2 знака след десетичната точка.

projection_type = input()
number_rows = int(input())
number_columns = int(input())

price = 0

if projection_type == 'Premiere':
    price = 12.00
elif projection_type == 'Normal':
    price = 7.50
elif projection_type == 'Discount':
    price = 5.00

total_revenue = number_columns * number_rows * price

print(f'{total_revenue:.2f} leva')