
product = input()
city = input()
quantity = float(input())

price = 0

if city == 'Sofia':
    if product == 'coffee':
        price = 0.50
        print(quantity * price)
    elif product == 'water':
        price = 0.80
        print(quantity * price)
    elif product == 'beer':
        price = 1.20
        print(quantity * price)
    elif product == 'sweets':
        price = 1.45
        print(quantity * price)
    elif product == 'peanuts':
        price = 1.60
        print(quantity * price)

elif city == 'Plovdiv':
    if product == 'coffee':
        price = 0.40
        print(quantity * price)
    elif product == 'water':
        price = 0.70
        print(quantity * price)
    elif product == 'beer':
        price = 1.15
        print(quantity * price)
    elif product == 'sweets':
        price = 1.30
        print(quantity * price)
    elif product == 'peanuts':
        price = 1.50
        print(quantity * price)

elif city == 'Varna':
    if product == 'coffee':
        price = 0.45
        print(quantity * price)
    elif product == 'water':
        price = 0.70
        print(quantity * price)
    elif product == 'beer':
        price = 1.10
        print(quantity * price)
    elif product == 'sweets':
        price = 1.35
        print(quantity * price)
    elif product == 'peanuts':
        price = 1.55
        print(quantity * price)
