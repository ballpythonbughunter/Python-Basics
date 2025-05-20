n = int(input())

sum_even = 0
sum_odd = 0

for i in range(n):
    current_number = int(input())

    if i % 2 == 0:
        sum_even += current_number

    else:
        sum_odd += current_number

if sum_odd == sum_even:
    print('Yes')
    print(f'Sum = {sum_even}')

else:
    diff = abs(sum_odd - sum_even)
    print('No')
    print(f'Diff = {diff}')