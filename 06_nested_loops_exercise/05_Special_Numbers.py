input_number = int(input())

for num in range(1_111, 10_000):

    number_as_str = str(num)

    is_special = True
    for digit in number_as_str:  # ['2', '4', '1', '8']
        digit_as_int = int(digit)  # int('2') == 2

        if digit_as_int == 0:
            is_special = False
            break

        if input_number % digit_as_int != 0:
            is_special = False
            break

    if is_special:
        print(num, end=' ')



