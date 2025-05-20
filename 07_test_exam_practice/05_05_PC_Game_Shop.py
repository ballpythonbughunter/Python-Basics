# Магазин за компютърни игри ви наема за да направите статистика на процента продажби на игрите от
# последния месец, като изчислите по колко процента от общите продажби са за някоя от игрите.
# Процентите трябва да бъдат разделени на четири части, три заглавия на игри и всички останали :
# • Hearthstone
# • Fornite
# • Overwatch
# • Others
#
# От конзолата се четат:
# • Брой продадени игри- n - цяло положително число в интервала [1… 100]
# За следващите n реда се чете по един ред:
# o Име на игра - текст

sold_games = int(input())

sales_counter_hearthstone = 0
sales_counter_fornite = 0
sales_counter_overwatch = 0
sales_counter_others = 0
sales_percentage = 0

for _ in range(sold_games):
    game_name = input()

    if game_name == 'Hearthstone':
        sales_counter_hearthstone += 1
    elif game_name == 'Fornite':
        sales_counter_fornite += 1
    elif game_name == 'Overwatch':
        sales_counter_overwatch += 1
    else:
        game_name = 'Others'
        sales_counter_others += 1

sales_percentage_hearthstone = sales_counter_hearthstone / sold_games * 100
sales_percentage_fornite = sales_counter_fornite / sold_games * 100
sales_percentage_overwatch = sales_counter_overwatch / sold_games * 100
sales_percentage_others = sales_counter_others / sold_games * 100

print(f"Hearthstone - {sales_percentage_hearthstone:.2f}%")
print(f"Fornite - {sales_percentage_fornite:.2f}%")
print(f"Overwatch - {sales_percentage_overwatch:.2f}%")
print(f"Others - {sales_percentage_others:.2f}%")

