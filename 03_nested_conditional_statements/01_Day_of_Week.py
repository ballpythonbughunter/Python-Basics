# Напишете програма, която чете цяло число, въведено от потребителя, и отпечатва ден от седмицата (на английски език),
# в граници [1...7] или отпечатва "Error" в случай, че въведеното число е невалидно.

day_of_the_week = int(input())

if day_of_the_week == 1:
    print(f'Monday')
elif day_of_the_week == 2:
    print(f'Tuesday')
elif day_of_the_week == 3:
    print(f'Wednesday')
elif day_of_the_week == 4:
    print(f'Thursday')
elif day_of_the_week == 5:
    print(f'Friday')
elif day_of_the_week == 6:
    print(f'Saturday')
elif day_of_the_week == 7:
    print(f'Sunday')
else:
    print(f'Error')
