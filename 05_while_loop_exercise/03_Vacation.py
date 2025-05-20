
money_needed = float(input())
available_money = float(input())
spend_counter = 0
day_counter = 0

while True:
    command = input() # "spend" or "save"
    activity_amount = float(input()) # sum that will be saved or spent
    day_counter += 1
    if command == 'save':
        spend_counter = 0
        available_money += activity_amount

    else:
        spend_counter += 1
        available_money -= activity_amount
        if available_money < 0:
            available_money = 0

    if spend_counter == 5:
        print("You can't save the money.")
        print(f"{day_counter}")
        break

    if available_money >= money_needed:
        print(f"You saved the money for {day_counter} days.")
        break














# money_needed = float(input())
# available_money = float(input())
# # money_counter = 0
# command_spend_counter = 0
# day_counter = 0
# # saved_activity_amount = 0
# # spent_activity_amount = 0
# final_amount = 0
#
# while True:
#     command = input() # "spend" or "save"
#     activity_amount = float(input()) # sum that will be saved or spent
#     day_counter += 1
#     if command == 'save':
#         command_spend_counter = 0
#         # saved_activity_amount += activity_amount
#         final_amount += activity_amount
#
#     else:
#         command_spend_counter += 1
#         if available_money - activity_amount < 0:
#             final_amount = 0
#         # spent_activity_amount += activity_amount
#         # final_amount -= activity_amount
#
#     if command_spend_counter == 5:
#         print("You can't save the money.")
#         print(f"{day_counter}")
#         break
#
#     if available_money + final_amount >= money_needed:
#         print(f"You saved the money for {day_counter} days.")
#         break

