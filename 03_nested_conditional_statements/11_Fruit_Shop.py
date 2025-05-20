# Магазин за плодове през работните дни работи на следните цени:
# плод banana apple orange grapefruit kiwi pineapple grapes
# цена 2.50     1.20 0.85     1.45     2.70  5.50     3.85

# През събота и неделя магазинът работи на по-високи цени:
# плод banana apple orange grapefruit kiwi pineapple grapes
# цена  2.70    1.25 0.90      1.60   3.00  5.60      4.20
# Напишете програма, която чете от конзолата следните три променливи, въведени от потребителя, и пресмята цената според цените от таблиците по-горе:
# · плод - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
# · ден от седмицата - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
# · количество (реално число).
# Резултатът да се отпечата закръглен с 2 цифри след десетичната точка. При невалиден ден от седмицата или невалидно име на плод да се отпечата "error".

fruit_type = input()
day_of_week = input()
amount = float(input())

if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
    if fruit_type == 'banana':
        banana = 2.50
        print(f'{amount * banana:.2f}')
    elif fruit_type == 'apple':
        apple = 1.20
        print(f'{amount * apple:.2f}')
    elif fruit_type == 'orange':
        orange = 0.85
        print(f'{amount * orange:.2f}')
    elif fruit_type == 'grapefruit':
        grapefruit = 1.45
        print(f'{amount * grapefruit:.2f}')
    elif fruit_type == 'kiwi':
        kiwi = 2.70
        print(f'{amount * kiwi:.2f}')
    elif fruit_type == 'pineapple':
        pineapple = 5.50
        print(f'{amount * pineapple:.2f}')
    elif fruit_type == 'grapes':
        grapes = 3.85
        print(f'{amount * grapes:.2f}')
    else:
        print('error')

elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    if fruit_type == 'banana':
        banana = 2.70
        print(f'{amount * banana:.2f}')
    elif fruit_type == 'apple':
        apple = 1.25
        print(f'{amount * apple:.2f}')
    elif fruit_type == 'orange':
        orange = 0.90
        print(f'{amount * orange:.2f}')
    elif fruit_type == 'grapefruit':
        grapefruit = 1.60
        print(f'{amount * grapefruit:.2f}')
    elif fruit_type == 'kiwi':
        kiwi = 3
        print(f'{amount * kiwi:.2f}')
    elif fruit_type == 'pineapple':
        pineapple = 5.60
        print(f'{amount * pineapple:.2f}')
    elif fruit_type == 'grapes':
        grapes = 4.20
        print(f'{amount * grapes:.2f}')
    else:
        print('error')
else:
    print('error')