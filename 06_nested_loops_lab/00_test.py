# LOOP THAT PRINTS NAME/WORD LETTERS ACCORDING TO ASCII TABLE NUMBERS:

while True:
    username = input()

    if username == 'Stop':
        break

    for letter in username:
        print(f'Letter {letter} -> ord() code: {ord(letter)}')