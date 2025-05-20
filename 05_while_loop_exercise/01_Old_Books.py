# Ани отива до родния си град след много дълъг период извън страната. Прибирайки се вкъщи, тя вижда старата библиотека
# на баба си и си спомня за любимата си книга. Помогнете на Ани, като напишете програма, в която тя въвежда търсената от
# нея книга (текст). Докато Ани не намери любимата си книга или не провери всички книги в библиотеката, програмата трябва
# да чете всеки път на нов ред името на всяка следваща книга (текст), която тя проверява. Книгите в библиотеката са свършили щом получите текст "No More Books".
# · Ако не открие търсената книгата да се отпечата на два реда:
#
# o "The book you search is not here!"
# o "You checked {брой} books."
# · Ако открие книгата си се отпечатва един ред:
# o "You checked {брой} books and found it."

# looking_for = input()
# counter = 0
#
# while True:
#     current_book = input()
#     if current_book != looking_for:
#         counter += 1
#         print("The book you search is not here!")
#         print(f"You checked {counter} books.")
#
#     elif current_book == looking_for:
#         print(f"You checked {counter} books and found it.")
#         break

looking_for = input() #e.g. Troy
command = input() #'No More Books' or books, e.g. 'Stronger'
counter = 0

while command != 'No More Books':
    current_book = command

    if current_book == looking_for:
        break

    counter += 1

    command = input()

if command == 'No More Books':
    print("The book you search is not here!")
    print(f"You checked {counter} books.")
else:
    print(f"You checked {counter} books and found it.")


# ALTERNATIVELY:


# looking_for = input() #e.g. Troy
# command = input() #'No More Books' or books, e.g. 'Stronger'
# counter = 0
# is_book_found = False
#
# while command != 'No More Books':
#     current_book = command
#
#     if current_book == looking_for:
#         is_book_found = True
#         break
#
#     counter += 1
#
#     command = input()
#
# if not is_book_found:
#     print("The book you search is not here!")
#     print(f"You checked {counter} books.")
# else:
#     print(f"You checked {counter} books and found it.")



