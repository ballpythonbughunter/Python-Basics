# От телевизионна компания ви наемат да създадете програма, която да изчислява дали за клиентите ще е
# възможно да си закупят желаните сериали. Разполагате с бюджет и брой сериали, които потребителят ще
# желае да закупи. Всеки сериал съответно има заглавие и цена.
# Някои от сериалите имат намаление:
# • Thrones – 50%
# • Lucifer – 40%
# • Protector – 30%
# • TotalDrama – 20%
# • Area – 10%

# От конзолата се четат:
# • Бюджет - реално число в интервала [10.0… 100.0]
# • Брой сериали - n - цяло положително число в интервала [1… 10]
# За всеки сериал се четат по два реда:
# o Име на сериал - текст
# o Цена за сериал - реално число в интервала [1.0… 15.0]

budget = float(input())
number_series = int(input())

discounted_price = 0
total_price = 0

for _ in range(number_series):
    name_series = input()
    price = float(input())

    if name_series == 'Thrones':
        discounted_price += price * 0.5
    elif name_series == 'Lucifer':
        discounted_price += price * 0.4
    elif name_series == 'Protector':
        discounted_price += price * 0.3
    elif name_series == 'TotalDrama':
        discounted_price += price * 0.2
    elif name_series == 'Area':
        discounted_price += price * 0.1

    total_price += price

total_price -= discounted_price

if budget >= total_price:
    print(f"You bought all the series and left with {(budget - total_price):.2f} lv.")
else:
    print(f"You need {(total_price - budget):.2f} lv. more to buy the series!")