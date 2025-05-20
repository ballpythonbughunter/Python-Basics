# По време на обедната почивка искате да изгледате епизод от своя любим сериал. Вашата задача е да напишете програма, с
# която ще разберете дали имате достатъчно време да изгледате епизода. По време на почивката отделяте време за обяд и
# време за отдих. Времето за обяд ще бъде 1/8 от времето за почивка, а времето за отдих ще бъде 1/4 от времето за почивка.
#
# 1. Име на сериал – текст
# 2. Продължителност на епизод – цяло число в диапазона [10… 90]
# 3. Продължителност на почивката – цяло число в диапазона [10… 120]
#
# · Ако времето е достатъчно да изгледате епизода:
# "You have enough time to watch {име на сериал} and left with {останало време} minutes free time."
#
# · Ако времето не Ви е достатъчно:
# "You don't have enough time to watch {име на сериал}, you need {нужно време} more minutes."

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
chill_time = break_duration / 4
time_left = break_duration - lunch_time - chill_time

import math

free_time = math.ceil(time_left - episode_duration)
needed_time = math.ceil(episode_duration - time_left)

if time_left >= episode_duration:
    print(f"You have enough time to watch {series_name} and left with {free_time} minutes free time.")

else:
    print(f"You don't have enough time to watch {series_name}, you need {needed_time} more minutes.")

