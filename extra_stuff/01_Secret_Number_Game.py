import random

secret_number = random.randint(1, 100)

attempts = 5

print('Welcome to SoftUni Python Basics game - The Number!')
print(f'You have {attempts} attempts to guess the number between 1 and 100\n')   #\n means give me new line

for attempt in range(1, attempts + 1):
    guess = int(input(f'Attempt {attempt} --> Enter your guess:'))

    if guess == secret_number:
        print(f'Congratulations! You guessed the number {secret_number} correctly in {attempt} attempts!')
        break
    elif guess < secret_number:
        print('Too low! Try again!')

    else:
        print('Too high! Try again!')

else:
    print(f'Sorry, you\'ve used all your {attempts}. The secret number was {secret_number}. Better luck next time!')






