# Дадено е цяло число – начален брой точки. Върху него се начисляват бонус точки по правилата, описани по-долу.
# Да се напише програма, която пресмята бонус точките, които получава числото и общия брой точки (числото + бонуса).
# · Ако числото е до 100 включително, бонус точките са 5;
# · Ако числото е по-голямо от 100 и по-малко или равно на 1000, бонус точките са 20% от числото;
# · Ако числото е по-голямо от 1000, бонус точките са 10% от числото.
# · Допълнителни бонус точки (начисляват се отделно от предходните):
# o За четно число à + 1 т.
# o За число, което завършва на 5 à + 2 т.

initial_points = int(input())
bonus_points = 0

if initial_points <= 100:
    bonus_points += 5
elif 100 < initial_points <= 1000:
    bonus_points += 0.2 * initial_points
elif initial_points > 1000:
    bonus_points += 0.1 * initial_points

if initial_points % 2 == 0:
    bonus_points = bonus_points + 1
elif initial_points % 10 == 5:
    bonus_points = bonus_points + 2

print(bonus_points)
print(initial_points + bonus_points)