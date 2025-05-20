# # Цени на играчките:
# # Пъзел - 2.60 лв.
#  Говореща кукла - 3 лв.
# Плюшено мече - 4.10 лв.
# Миньон - 8.20 лв.
# Камионче - 2 лв.
# # Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена. От спечелените пари Петя трябва да
# даде 10% за наема на магазина. Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.

# 1. Цена на екскурзията - реално число в интервала [1.00 … 10000.00]
# 2. Брой пъзели - цяло число в интервала [0… 1000]
# 3. Брой говорещи кукли - цяло число в интервала [0 … 1000]
# 4. Брой плюшени мечета - цяло число в интервала [0 … 1000]
# 5. Брой миньони - цяло число в интервала [0 … 1000]
# 6. Брой камиончета - цяло число в интервала [0 … 1000]

holiday_price = float(input())
puzzles = int(input())
speaking_toys = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

ordered_toys = puzzles + speaking_toys + teddy_bears + minions + trucks

# puzzle_price = 2.60
# speaking_toy_price = 3
# teddy_bear_price = 4.10
# minion_price = 8.20
# truck_price = 2

final_order_price = puzzles * 2.60 + speaking_toys * 3 + teddy_bears * 4.10 + minions * 8.20 + trucks * 2

if ordered_toys >= 50:
    final_order_price -= final_order_price * 0.25

final_amount = final_order_price * 0.9
money_left = (final_amount - holiday_price)

if final_amount >= holiday_price:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    missing_amount = abs(money_left)
    print(f"Not enough money! {missing_amount:.2f} lv needed.")