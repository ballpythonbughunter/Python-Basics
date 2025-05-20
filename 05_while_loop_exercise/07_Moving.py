width = int(input())
length = int(input())
height = int(input())

total_space_left = width * length * height

while True:
    command = input()

    if command == 'Done':
        break

    space = int(command)

    total_space_left -= space
    if total_space_left <= 0:
        break

if total_space_left < 0:
    print(f"No more free space! You need {-total_space_left} Cubic meters more.")
else:
    print(f"{total_space_left} Cubic meters left.")