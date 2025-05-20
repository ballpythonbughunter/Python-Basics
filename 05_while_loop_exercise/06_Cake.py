width = int(input())
length = int(input())

total_pieces = width * length

while True:
    command = input()

    if command == 'STOP':
        break

    current_pieces = int(command)

    total_pieces -= current_pieces

    if total_pieces <= 0:
        break

if total_pieces > 0:
    print(f"{total_pieces} pieces are left.")

else:
    print(f"No more cake left! You need {-total_pieces} pieces more.")


