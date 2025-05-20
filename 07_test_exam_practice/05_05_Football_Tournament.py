# Задачата ви е да напишете програма, която приема името на отбор и прави статистика за него. През
# един сезон всеки отбор изиграва определен брой футболни срещи, като за всяка среща на отбора
# се дават точки в зависимост от изхода от срещата. Има три възможни изхода от една среща:
# ▪ W - Отборът е победител и получава 3 точки
# ▪ D - Срещата е завършила без победител и отборът получава 1 точка
# ▪ L - Отборът е загубил срещата и не получава точки
# Напишете програма, която приема името на футболен отбор и извежда неговата статистика, на база
# на изиграните срещи през този сезон. Неговата статистика трябва да включва общия брой
# спечелени точки през настоящия сезон, подробна статистика за изхода на изиграните игри и
# процент победи през сезона. Ако отборът по някаква причина не е играл мачове през настоящия
# сезон се извежда специално съобщение.

# От конзолата се четат два реда:
# • Името на футболния отбор, за който водим статистика - текст
# • Броя изиграни срещи през настоящия сезон - цяло число в интервала [0… 100]
# За всяка изиграна среща се прочита отделен ред:
# o Резултатът от изиграната среща в един от горепосочените формати – символ с
# възможности 'W', 'D' и 'L'


team_name = input()
played_games = int(input())

counter_points = 0
won_counter = 0
draw_counter = 0
lost_counter = 0
total_points = 0
percentage_won = 0

for _ in range(played_games):
    game_result = input()

    if game_result == 'W':
        counter_points += 3
        won_counter += 1
    elif game_result == 'D':
        counter_points += 1
        draw_counter += 1
    elif game_result == 'L':
        lost_counter += 1

    total_points = counter_points
    percentage_won = won_counter / played_games * 100

if played_games == 0:
    print(f"{team_name} hasn't played any games during this season.")

else:
    print(f"{team_name} has won {total_points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {won_counter}")
    print(f"## D: {draw_counter}")
    print(f"## L: {lost_counter}")
    print(f"Win rate: {percentage_won:.2f}%")