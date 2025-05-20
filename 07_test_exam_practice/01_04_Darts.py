initial_points = 301
negative_shots = 0
positive_shots = 0

player_name = input()

while True:
    field = input()
    points = int(input())

    if field == "Single":
        initial_points -= points
        if initial_points < 0:
            negative_shots += 1
        elif initial_points > 0:
            positive_shots +=1
        elif initial_points == 0:
            positive_shots += 1
            player_won = player_name
            print(f"{player_won} won the leg with {positive_shots} shots.")
            break

    elif field == "Double":
        initial_points -= 2 * points
        if initial_points < 0:
            negative_shots += 1
        elif initial_points > 0:
            positive_shots += 1
        elif initial_points == 0:
            positive_shots += 1
            player_won = player_name
            print(f"{player_won} won the leg with {positive_shots} shots.")
            break

    elif field == "Triple":
        initial_points -= 3 * points
        if initial_points < 0:
            negative_shots += 1
        elif initial_points > 0:
            positive_shots += 1
        elif initial_points == 0:
            positive_shots += 1
            player_won = player_name
            print(f"{player_won} won the leg with {positive_shots} shots.")
            break

    elif field == "Retire":
        player_retire = player_name
        print(f"{player_retire} retired after {negative_shots} unsuccessful shots.")
        break



