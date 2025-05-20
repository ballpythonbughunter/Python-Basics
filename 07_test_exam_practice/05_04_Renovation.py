wall_height = int(input())
wall_length = int(input())
not_painting = int(input())
painted_area = 0
painting_area = 0

while True:
    command = input()
    full_area = wall_length * wall_height * 4
    painting_area = full_area - full_area * not_painting / 100
    if command == "Tired!":
        print(f"{round(painting_area - painted_area)} quadratic m left.")
        break

    else:
        paint_amount = int(command)
        painted_area += paint_amount

        if painting_area < painted_area:
            print(f"All walls are painted and you have {round(painted_area - painting_area)} l paint left!")
            break

        elif painting_area == painted_area:
            print("All walls are painted! Great job, Pesho!")
            break




