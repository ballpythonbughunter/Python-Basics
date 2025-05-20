# Напишете програма която, чете ден от седмицата (текст), на английски език - въведен от потребителя.Ако денят е работен
# отпечатва на конзолата - "Working day", ако е почивен - "Weekend". Ако се въведе текст различен от ден от седмицата да
# се отпечата - "Error".


# day_of_the_week = input()
#
#
# if day_of_the_week in ('Monday','Tuesday','Wednesday','Thursday','Friday'):
#     print('Working day')
# elif day_of_the_week in ('Saturday', 'Sunday'):
#     print('Weekend')
# else:
#     print('Error')

# --------------------------------------------------------------------

day_of_the_week = input()

if day_of_the_week == 'Monday':
    print('Working day')
elif day_of_the_week == 'Tuesday':
    print('Working day')
elif day_of_the_week == 'Wednesday':
    print('Working day')
elif day_of_the_week == 'Thursday':
    print('Working day')
elif day_of_the_week == 'Friday':
    print('Working day')
elif day_of_the_week == 'Saturday':
    print('Weekend')
elif day_of_the_week == 'Sunday':
    print('Weekend')
else:
    print('Error')
