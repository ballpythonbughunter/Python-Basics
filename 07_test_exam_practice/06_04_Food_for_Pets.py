days = int(input())
total_food = float(input())

total_eaten_biscuits = 0
total_eaten_food = 0
total_food_dog = 0
total_food_cat = 0

for day in range(1, days + 1):
    food_dog = int(input())
    food_cat = int(input())

    total_eaten_food += food_dog + food_cat

    if day % 3 == 0:
        total_eaten_biscuits += (food_dog + food_cat) * 0.1

    total_food_dog += food_dog
    total_food_cat += food_cat

print(f"Total eaten biscuits: {round(total_eaten_biscuits)}gr.")
print(f"{(total_eaten_food / total_food * 100):.2f}% of the food has been eaten.")
print(f"{((total_food_dog / total_eaten_food) * 100):.2f}% eaten from the dog.")
print(f"{(total_food_cat / total_eaten_food * 100):.2f}% eaten from the cat.")