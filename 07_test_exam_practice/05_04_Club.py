desired_profit = float(input())
order_total = 0

while True:
    command = input()
    if command == "Party!":
        missing_amount = desired_profit - order_total
        print(f"We need {missing_amount:.2f} leva more.")
        print(f"Club income - {order_total:.2f} leva.")
        break

    else:
        cocktail_name = command
        cocktails_per_order = int(input())
        cocktail_price = len(cocktail_name)
        current_order_price = cocktails_per_order * cocktail_price

        if current_order_price % 2 != 0:
            current_order_price -= current_order_price * 0.25

        order_total += current_order_price

    if order_total >= desired_profit:
        print("Target acquired.")
        print(f"Club income - {order_total:.2f} leva.")
        break
