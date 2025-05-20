# Деси много обича да гледа филми, но често й е трудно да си избере подходящ за гледане. Набелязва си
# определен брой филми и иска да си избере кой филм да гледа спрямо рейтинга на филмите.
# Напишете програма, която показва кой филм е с най-висок рейтинг, кой е с най-нисък и колко е средният
# рейтинг от всички филми, които си е набелязала да гледа.
#
# От конзолата първо се чете един ред:
# • Брой филми, които си е набелязала Деси – цяло число в интервала [1…20]
# За всеки филм се прочитат два отделни реда:
# • Име на филма – текст
# • Рейтинг на филма - реално число в интервала [1.00…10.00]
import sys

number_movies = int(input())

highest_rating = -sys.maxsize
lowest_rating = sys.maxsize
highest_rating_name = ''
lowest_rating_name = ''
all_ratings = 0

for _ in range(number_movies):
    movie_name = input()
    movie_rating = float(input())

    all_ratings += movie_rating

    if movie_rating > highest_rating:
        highest_rating = movie_rating
        highest_rating_name = movie_name

    elif movie_rating < lowest_rating:
        lowest_rating = movie_rating
        lowest_rating_name = movie_name

average_rating = all_ratings / number_movies

print(f'{highest_rating_name} is with highest rating: {highest_rating:.1f}')
print(f'{lowest_rating_name} is with lowest rating: {lowest_rating:.1f}')
print(f'Average rating: {average_rating:.1f}')


