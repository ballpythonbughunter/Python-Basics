#1. Брой страници в текущата книга – цяло число в интервала [1…1000]
#2. Страници, които прочита за 1 час – цяло число в интервала [1…1000]
#3. Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]

number_pages = int(input())
pages_per_hour = int(input())
total_amount_days = int(input())

total_hours_to_read_one_book = number_pages // pages_per_hour

hours_per_day = total_hours_to_read_one_book / total_amount_days

print(hours_per_day)