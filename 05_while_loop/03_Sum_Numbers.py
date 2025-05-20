init_number = int(input())

sum_num = 0

while True:
    current_number = int(input())
    sum_num += current_number
    if sum_num >= init_number:
        print(sum_num)
        break

