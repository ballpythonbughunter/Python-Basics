first_num = int(input())
last_num = int(input())
magical_num = int(input())

combination_counter = 0
flag = False

for i in range(first_num, last_num + 1):
    for y in range(first_num, last_num + 1):
        combination_counter += 1
        if i + y == magical_num:
            print(f"Combination N:{combination_counter} ({i} + {y} = {magical_num})")
            flag = True
            break

    if flag:
        break

else:
    print(f"{combination_counter} combinations - neither equals {magical_num}")