

N_days = int(input())

total_rakiya = 0
total_degrees = 0

for _ in range(N_days):
    rakiya_amount = float(input())
    drink_degrees = float(input())

    total_rakiya += rakiya_amount
    total_degrees += rakiya_amount * drink_degrees

degree_average = total_degrees / total_rakiya

print(f"Liter: {total_rakiya:.2f}")
print(f"Degrees: {degree_average:.2f}")

if degree_average < 38:
    print("Not good, you should baking!")
elif 38 < degree_average < 42:
    print("Super!")
else:
    print("Dilution with distilled water!")
