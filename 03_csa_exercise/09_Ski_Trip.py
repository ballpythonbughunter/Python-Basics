# "room for one person" – 18.00 лв за нощувка
# § "apartment" – 25.00 лв за нощувка
# § "president apartment" – 35.00 лв за нощувка

# Според броят на дните, в които ще остане в хотела (пример: 11 дни = 10 нощувки) и видът на помещението, което ще избере, той може да ползва различно намаление.
# Намаленията са както следва:
# вид помещение           по-малко от 10 дни      между 10 и 15 дни       повече от 15 дни
# room for one person    не ползва намаление     не ползва намаление      не ползва намаление

# apartment              30% от крайната цена    35% от крайната цена     50% от крайната цена
# president apartment    10% от крайната цена    15% от крайната цена     20% от крайната цена

# След престоя, оценката на Атанас за услугите на хотела може да е позитивна (positive) или негативна (negative) .
# Ако оценката му е позитивна, към цената с вече приспаднатото намаление Атанас добавя 25% от нея. Ако оценката му е негативна приспада от цената 10%.

days_stay = int(input())
type_stay = input()
rating = input()

nights = days_stay - 1
price = 0.00
discount = 0.00

if type_stay == 'room for one person':
    price = 18.00

elif type_stay == 'apartment':
    price = 25.00
    if nights < 10:
        price -= price * 0.30
    elif nights <= 15:
        price -= price * 0.35
    else:
        price -= price * 0.50

elif type_stay == 'president apartment':
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