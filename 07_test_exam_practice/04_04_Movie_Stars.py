budget = float(input())
budget_left = budget

while True:
    command = input()
    if command == "ACTION":
        print(f"We are left with {budget_left:.2f} leva.")
        break

    actor_name = command
    if len(actor_name) <= 15:
        reward = float(input())
    else:
        reward = budget_left * 0.2
    budget_left -= reward

    if budget_left < 0:
        print(f"We need {abs(budget_left):.2f} leva for our actors.")
        break