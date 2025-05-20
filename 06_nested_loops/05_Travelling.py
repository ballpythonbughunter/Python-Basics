

while True:
    destination = input()

    if destination == 'End':
        break

    min_budget = float(input())
    savings = 0

    while savings < min_budget:
        savings += float(input())

    print(f"Going to {destination}!")