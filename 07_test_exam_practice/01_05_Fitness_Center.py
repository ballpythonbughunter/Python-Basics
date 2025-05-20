# Напишете програма, която да изчислява броя на посетителите в един фитнес център. В началото програмата
# получава броя на посетителите на фитнеса и за всеки човек - дейността, която извършва във фитнеса. На края
# програмата трябва да отпечата броят трениращи за всяка една дейност ("Back", "Chest", 'Legs", "Abs")и броят
# клиенти, закупили продукт ("Protein shake", "Protein bar"). Също така - процентът трениращи (спрямо общия
# брой посетители) и процентът на клиентите, закупили продукт от фитнеса.
#
# От конзолата се чете число, след това поредица от низове, всяко на отделен ред:
# • На първия ред – броят на посетителите във фитнеса – цяло число в интервала [1...1000]
# • За всеки един посетител на отделен ред – дейността във фитнеса – текст ("Back", "Chest", "Legs", "Abs",
# "Protein shake" или "Protein bar")
#
# Да се отпечатат на конзолата 8 реда, които съдържат следната информация:
# Ред 1 - "{брой хора трениращи гръб} - back"
# Ред 2 - "{брой хора трениращи гърди} - chest"
# Ред 3 - "{брой хора трениращи крака} - legs"
# Ред 4 - "{брой хора трениращи коремни мускули} - abs"
# Ред 5 - "{брой хора закупили протеинов шейк} - protein shake"
# Ред 6 - "{брой хора закупили протеинов блок} - protein bar"
# Ред 7 - "{процент на хората дошли да тренират}% - work out"
# Ред 8 - "{процент на хората дошли да купят протеин}% - protein"


number_visitors = int(input())

back_count = 0
chest_count = 0
legs_count = 0
abs_count = 0
protein_shake_count = 0
protein_bar_count = 0

for _ in range(number_visitors):
    activity = input()

    if activity == 'Back':
        back_count +=1
    elif activity == 'Chest':
        chest_count +=1
    elif activity == 'Legs':
        legs_count +=1
    elif activity == 'Abs':
        abs_count +=1
    elif activity == 'Protein shake':
        protein_shake_count +=1
    elif activity == 'Protein bar':
        protein_bar_count +=1

total_trainers = back_count + chest_count + legs_count + abs_count
total_buyers = protein_bar_count + protein_shake_count
percentage_trainers = total_trainers / number_visitors * 100
percentage_buyers = total_buyers / number_visitors * 100


print(f"{back_count} - back")
print(f"{chest_count} - chest")
print(f"{legs_count} - legs")
print(f"{abs_count} - abs")
print(f"{protein_shake_count} - protein shake")
print(f"{protein_bar_count} - protein bar")
print(f"{percentage_trainers:.2f}% - work out")
print(f"{percentage_buyers:.2f}% - protein")

