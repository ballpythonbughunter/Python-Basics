# конзолна програма, която чете оценка (реално число), въведена от потребителя и отпечатва "Excellent!",
# ако оценката е 5.50 или по-висока.

grade = float(input())

if grade >= 5.5:
    print('Excellent!')
elif grade < 5.5:
    print("It's actually too low")