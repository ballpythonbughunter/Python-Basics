# Остават 5 дни до рождения ден на брата на Тереза. Тя иска да му купи подарък и решава да си направи малък щанд и да
# продава плетени гривнички с мъниста, за да събере достатъчно пари.
# Вашата задача е да напишете програма, която да изчислява сумата, която Тереза е успяла да събере и да даде отговор на
# момичето, дали тя ще може да купи подарък или не. Трябва да се вземат предвид нейните разходи и цената на подаръка.


pocket_money = float(input())
sales_profit = float(input())
total_spent = float(input())
present_price = float(input())

days_left = 5

saved_pocket = days_left * pocket_money
profit_money = days_left * sales_profit
total_saved = saved_pocket + profit_money
final_left = total_saved - total_spent

if final_left >= present_price:
    print(f"Profit: {final_left:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {present_price - final_left:.2f} BGN.")
