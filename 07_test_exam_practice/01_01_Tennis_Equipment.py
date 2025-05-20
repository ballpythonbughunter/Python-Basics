#той трябва да заплати 1/8 от цената, а останалите 7/8 трябва да бъдат заплатени от неговите спонсори.
#Джокович иска да закупи n на брой тенис ракети и m чифта маратонки, както и друга екипировка, на стойност 20%
# от общата цена на закупените ракети и маратонки.

#•	"Price to be paid by Djokovic {1/8 от общата цена, закръглена към по-малкото цяло число}"
#•	"Price to be paid by sponsors {7/8 от общата цена, закръглена към по-голямото цяло число}"



price_per_tennis_racket = float(input())
number_tennis_rackets = int(input())
number_sneakers = int(input())

from math import floor, ceil

price_per_sneakers = price_per_tennis_racket / 6
price_other_stuff = (price_per_tennis_racket * number_tennis_rackets + price_per_sneakers * number_sneakers) * 0.2
total_price = price_per_tennis_racket * number_tennis_rackets + price_per_sneakers * number_sneakers + price_other_stuff

print(f"Price to be paid by Djokovic {floor(1/8 * total_price)}")
print(f"Price to be paid by sponsors {ceil(7/8 * total_price)}")

