max_goals = 0
best_player = ''

while True:
    command = input()
    if command == "END":
        break

    player_name = command
    goals_scored = int(input())

    if goals_scored > max_goals:
        max_goals = goals_scored
        best_player = player_name

    if goals_scored >= 10:
        break

print(f"{best_player} is the best player!")

if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")

else:
    print(f"He has scored {max_goals} goals.")
