# •	Първи ред – дни за престой – цяло число в интервала [0...365]
# •	Втори ред –  вид помещение –  "room for one person",  "apartment" или "president apartment"
# •	Трети ред –  оценка - "positive"  или "negative"

days_stay = int(input())
stay_type = input()
rating = input()

nights = days_stay - 1
price = 0.00
discount = 0.00

if stay_type == 'room for one person':
    price = 18.00

elif stay_type == 'apartment':
    price = 25.00
    if nights < 10:
        price -= price * 0.30
    elif nights <= 15:
        price -= price * 0.35
    else:
        price -= price * 0.50

elif stay_type == 'president apartment':
    price = 35.00
    if nights < 10:
        price -= price * 0.10
    elif 10 < nights < 15:
        price -= price * 0.15
    else:
        price -= price * 0.20

if rating == 'positive':
    discount = -0.25
elif rating == 'negative':
    discount = 0.10

final_price = price * nights * (1 - discount)

print(f'{final_price:.2f}')