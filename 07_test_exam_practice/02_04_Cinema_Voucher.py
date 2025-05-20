voucher_value = int(input())
movie_tickets = 0
other_purchases = 0

while True:
    chosen_purchase = input()
    if len(chosen_purchase) > 8:
        current_purchase_price = ord(chosen_purchase[0]) + ord(chosen_purchase[1])
        if current_purchase_price <= voucher_value:
            movie_tickets += 1
            voucher_value -= current_purchase_price
        elif current_purchase_price > voucher_value:
            print(movie_tickets)
            print(other_purchases)
            break
    elif chosen_purchase == "End":
        print(movie_tickets)
        print(other_purchases)
        break
    elif len(chosen_purchase) <= 8:
        current_purchase_price = ord(chosen_purchase[0])
        if current_purchase_price <= voucher_value:
            other_purchases += 1
            voucher_value -= current_purchase_price
        elif current_purchase_price > voucher_value:
            print(movie_tickets)
            print(other_purchases)
            break


