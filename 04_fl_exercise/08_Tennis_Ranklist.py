# Григор Димитров е тенисист, чиято следваща цел е изкачването в световната ранглиста по тенис за мъже.
# През годината Гришо участва в определен брой турнири, като за всеки турнир получава точки, които зависят от позицията, на която е завършил в турнира. Има три варианта за завършване на турнир:
# § W - ако е победител получава 2000 точки
# § F - ако е финалист получава 1200 точки
# § SF - ако е полуфиналист получава 720 точки
# Напишете програма, която изчислява колко ще са точките на Григор след изиграване на всички турнири, като знаете с колко точки стартира сезона.
# Също изчислете колко точки средно печели от всички изиграни турнири и колко процента от турнирите е спечелил.
# От конзолата първо се четат два реда:
#
# · Брой турнири, в които е участвал – цяло число в интервала [1…20]
# · Начален брой точки в ранглистата - цяло число в интервала [1...4000]
# За всеки турнир се прочита отделен ред:
# · Достигнат етап от турнира – текст – "W", "F" или "SF"
import math

number_tournaments = int(input())
initial_points = int(input())

tournament_points = 0
tournament_counter = 0
tournaments_won = 0

for _ in range(number_tournaments):
    current_tournament = input()

    if current_tournament == "W":
        tournament_points += 2000
        tournament_counter += 1
        tournaments_won = tournament_counter
    elif current_tournament == "F":
        tournament_points += 1200
    elif current_tournament == 'SF':
        tournament_points += 720

final_points = initial_points + tournament_points

print(f"Final points: {final_points}")

print(f"Average points: {math.floor(tournament_points/number_tournaments)}")

print(f'{((tournaments_won/number_tournaments) * 100):.2f}%')


































