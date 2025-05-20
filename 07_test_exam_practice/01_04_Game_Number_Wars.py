first_player = input()
second_player = input()
points_player_one = 0
points_player_two = 0

while True:
    card_player_one = input()

    if card_player_one != "End of game":
        card_player_one = int(card_player_one)
        card_player_two = int(input())
        if card_player_one > card_player_two:
            points = card_player_one - card_player_two
            points_player_one += points

        elif card_player_one < card_player_two:
            points = card_player_two - card_player_one
            points_player_two += points

        elif card_player_one == card_player_two:
            print("Number wars!")
            card_player_one = int(input())
            card_player_two = int(input())
            if card_player_one > card_player_two:
                print(f"{first_player} is winner with {points_player_one} points")
                break
            else:
                print(f"{second_player} is winner with {points_player_two} points")
                break

    else:
        print(f"{first_player} has {points_player_one} points")
        print(f"{second_player} has {points_player_two} points")
        break


