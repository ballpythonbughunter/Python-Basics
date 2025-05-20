input_command = input()
sum_prime_numbers = 0
sum_composite_numbers = 0

while input_command != 'stop':
    number = int(input_command)

    if number < 0:
        print("Number is negative.")
        input_command = input()
        continue

    is_prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        sum_prime_numbers += number
    else:
        sum_composite_numbers += number

    input_command = input()

print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_composite_numbers}")