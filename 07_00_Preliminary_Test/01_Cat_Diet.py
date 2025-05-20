# •	Процент на мазнините - цяло число в интервала [0…100]
# •	Процент на протеините - цяло число в интервала [0…100]
# •	Процент на въглехидратите - цяло число в интервала [0…100]
# •	Общ брой калории - цяло число в интервала [1000…15000]
# •	Процент на съдържанието на вода - цяло число в интервала [0…100]

percent_fats = int(input())
percent_proteins = int(input())
percent_carbs = int(input())
total_calories = int(input())
water_percentage = int(input())

fats_gram_cal = 9
proteins_gram_cal = 4
carbs_gram_cal = 4

total_fat_gram = (percent_fats * total_calories / fats_gram_cal) / 100
total_prot_gram = (percent_proteins * total_calories / proteins_gram_cal) / 100
total_carb_gram = (percent_carbs * total_calories / carbs_gram_cal) / 100

total_weight = total_fat_gram + total_prot_gram + total_carb_gram
calories_per_gram = total_calories / total_weight
calories = calories_per_gram * (1 - water_percentage / 100)

print(f"{calories:.4f}")