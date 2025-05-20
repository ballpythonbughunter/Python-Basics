daily_goal = int(input())
profit_counter = 0
is_target_reached = False

haircut_mens = 15
haircut_ladies = 20
haircut_kids = 10
paint_touch_up = 20
paint_full_color = 30

while True:
    if profit_counter >= daily_goal:
        print("You have reached your target for the day!")
        break

    command = input()

    if command == 'closed':
        print(f"Target not reached! You need {daily_goal - profit_counter}lv. more.")
        break

    if command == 'haircut':
        haircut_style = input()
        if haircut_style == 'mens':
            profit_counter += haircut_mens
        elif haircut_style == 'ladies':
            profit_counter += haircut_ladies
        elif haircut_style == 'kids':
            profit_counter += haircut_kids
    if command == 'color':
        paint_type = input()
        if paint_type == 'touch up':
            profit_counter += paint_touch_up
        elif paint_type == 'full color':
            profit_counter += paint_full_color

print(f"Earned money: {profit_counter}lv.")



