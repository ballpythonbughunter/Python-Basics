
total_steps = 0
one_direction = 0

while True:
    command = input()

    if command != "Going home":
        one_direction = int(command)
        total_steps += one_direction
        if total_steps >= 10000:  # goal reached
            break
    else:
        command = input()
        steps_back = int(command)
        total_steps += steps_back
        break

if total_steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{total_steps - 10000} steps over the goal!")

else:
    print(f"{10000 - total_steps} more steps to reach goal.")




