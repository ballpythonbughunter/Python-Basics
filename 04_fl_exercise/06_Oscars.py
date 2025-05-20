# Поканени сте от академията да напишете софтуер, който да пресмята точките за актьор/актриса. Академията ще ви даде първоначални точки за актьора.
# След това всеки оценяващ ще дава своята оценка. Точките, които актьора получава се формират от: дължината на името на оценяващия умножено по точките, които дава делено на две.
# Ако резултатът в някой момент надхвърли 1250.5 програмата трябва да прекъсне и да се отпечата, че дадения актьор е получил номинация.
# • Име на актьора - текст
# • Точки от академията - реално число в интервала [2.0... 450.5]
# • Брой оценяващи n - цяло число в интервала[1… 20]
# На следващите n-на брой реда: o Име на оценяващия - текст
# o Точки от оценяващия - реално число в интервала [1.0... 50.0

actor_name = input()
academy_points = float(input())
number_jury = int(input())

total_points = 0
total_jury_points = 0

for _ in range(number_jury):
    name_jury = input()
    points_jury = float(input())

    total_jury_points += len(name_jury) * points_jury / 2

    total_points = academy_points + total_jury_points

    if total_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break
else:
    print(f"Sorry, {actor_name} you need {(1250.5 - total_points):.1f} more!")