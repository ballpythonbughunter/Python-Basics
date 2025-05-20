hall_capacity = int(input())
number_customers = 0
total_income = 0
seats_left = hall_capacity

while True:
    command = input()

    if command != "Movie time!":
        incoming_customers = int(command)
        number_customers += incoming_customers
        seats_left = hall_capacity - number_customers
        if seats_left < 0:
            print("The cinema is full.")
            print(f"Cinema income - {total_income} lv.")
            break
        else:
            if incoming_customers % 3 == 0:
                current_payment = incoming_customers * 5 - 5
            else:
                current_payment = incoming_customers * 5
            total_income += current_payment
    else:
        print(f"There are {seats_left} seats left in the cinema.")
        print(f"Cinema income - {total_income} lv.")
        break
