# Хотел предлага 2 вида стаи: студио и апартамент. Напишете програма, която изчислява цената за целия престой за студио и апартамент. Цените зависят от месеца на престоя:
# Май и октомври Юни и септември Юли и август
# Студио - 50 лв./нощувка Студио - 75.20 лв./нощувка Студио - 76 лв./нощувка
# Апартамент - 65 лв./нощувка Апартамент - 68.70 лв./нощувка Апартамент - 77 лв./нощувка
# Предлагат се и следните отстъпки:· За студио, при повече от 7 нощувки през май и октомври : 5% намаление.· За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
# · За студио, при повече от 14 нощувки през юни и септември: 20% намаление.· За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.

# Входът се чете от конзолата и съдържа точно 2 реда, въведени от потребителя:· На първия ред е месецът - May, June, July, August, September или October;· На втория ред е броят на нощувките - цяло число.
# Да се отпечатат на конзолата 2 реда:· На първия ред: "Apartment: {цена за целият престой} lv." · На втория ред: "Studio: {цена за целият престой} lv." Цената за целия престой да е с до два знака след запетая.


month = input()
number_nights = int(input())

studio_price = 0.00
apartment_price = 0.00

if month == 'May' or month == 'October':
    studio_price = 50.00
    apartment_price = 65.00
    if number_nights > 14:
        studio_price -= studio_price * 0.30
        apartment_price -= apartment_price * 0.10
    elif number_nights > 7:
        studio_price -= studio_price * 0.05

elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
    if number_nights > 14:
        studio_price -= studio_price * 0.20
        apartment_price -= apartment_price * 0.10

elif month == 'July' or month == 'August':
    studio_price = 76.00
    apartment_price = 77.00
    if number_nights > 14:
        apartment_price -= apartment_price * 0.10

total_apartment_price = number_nights * apartment_price
total_studio_price = number_nights * studio_price

print(f"Apartment: {total_apartment_price:.2f} lv.")
print(f"Studio: {total_studio_price:.2f} lv.")