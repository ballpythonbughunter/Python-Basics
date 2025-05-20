#
# PRINT ALL NUMBERS UNTIL N WITH AN INTERVAL OF 3:
#
# n = int(input())
#
# for i in range(1, n + 1, 3):
#     print(i)
#
#
# PRINT EVERY SECOND POWER OF 2:
#
# n = int(input())
# num = 1
#
# for i in range(0, n + 1, 2):
#     print(num)
#     num = num * 2 * 2
#
# ALTERNATIVELY:
#
# n = int(input())
#
# for i in range(n + 1):
#     if i % 2 == 0:
#         print(2**i)
#
# #
# PRINT 'NUMBER IS -' AND NUMBER WITH CHOSEN INTERVAL:
#
# for num in range(10, 111, 20):
#     print('number is - ', num)
#
#
# PRINT LENGTH OF WORD IN NUMBERS ONE UNDER ANOTHER:
#
# word = 'SoftUni'
#
# for i in range(1, len(word) + 1):
#     print(i)
#
# PRINT WORD LETTERS ONE UNDER ANOTHER WITH INDEXED NUMBERS AFTER A DASH:
#
# word = 'SoftUni'
#
# for i in range(len(word)):
#     print(f'{word[i]} - ', i)
#
# PRINT ALL TEXT LETTERS ONE UNDER ANOTHER:
#
# for letter in 'Python':
#     print(letter)
#
# == same as below:
# word = 'Python'
# #
# for i in word:
#     print(i)
#
# PRINT SAME TEXT N TIMES:
#
# for _ in range(5):
#     print('SoftUni')
#
# BREAK:
#
# for number in range(1, 11):
#     if number == 5:
#         break
#     print('number is - ', number)
#
# CONTINUE - PRINT ALL NUMBER WITHOUT N == 5:
#
# for number in range(1, 11):
#     if number == 5:
#         continue
#     print('number is - ', number)
#
# CONTINUE - PRINT ALL NUMBERS WITHOUT EVENS:
#
# for number in range(1, 11):
#     if number % 2 == 0:
#         continue
#     print('number is - ', number)
#
# CONTINUE - PRINT ALL NUMBERS WITHOUT ODDS:
#
# for number in range(1, 11):
#     if number % 2 != 0:
#         continue
#     print('number is - ', number)
#
# PRINT NUMBERS IN REVERSE SEQUENCE:
#
# for number in range(20, 9, -1):
#     print(number)
#
# or
#
# for number in range(5, -11, -1):
#     print(number)
#
# PRINT SAME AS ABOVE ON ONE ROW:
#
# for number in range(5, -11, -1):
#     print(number, end = ' ')
#
#
# PRINTS INDEXES OF EACH LETTERS:
#
# text = input()
#
# for i in range(len(text)):
#     print('Index:', i, '-->', 'Letter:', text[i])
# alternatively:
#     print(f'Index: {i} --> Letter: {text[i]}')
#
#
#
# text = input()
#
# for i in range(len(text)):
#     print(text[i])
#
# for _ in range(5):
#     print('Cool')
#
# BREAK AND CONTINUE:
#
# for _ in range(5):
#     username = input()
#
#     if username == "Admin123":
#     print('Admin 123 end of loop with break!')
# #         break
#     else:
#       print(f'Welcome, {usermane}!')
#
# else:
#   print('End of loop')
#
#
# CONTINUE:
#
# for _ in range(5):
#     username = input()
#
#     if username == "Admin123":
#         continue
#         # print('Welcome, Admin123!')
#
#     else:
#         print(f'Welcome, {username}!')
#
#
# FINDING AN ELEMENT:
#
# search_element = 'Softuni'
#
# for _ in range(5):
#     element = input()
#
#     if element == search_element:
#         print('Element found!')
# else:
#     print('Element not found!')
#
#

# PRINTING EACH DIGITS OF A NUMBER ONE UNDER ANOTHER:

# number = 9876
# number_as_string = str(number)
#
# for digit in number_as_string:
#     print(digit)
#
#     # ---
#     print(type(digit))
#     # to change type back to integer we need to cast it accordingly:
#     digit_as_integer = int(digit)
#     print(type(digit_as_integer))
#     print(digit_as_integer * 100)

# ENUMERATE:

# name = 'Simo'
#
# for ch in name:
#     print(ch)
# ---
# name = 'Simo'
# counter = 0
#
# for ch in name:
#     print(f'char = {ch}, idx = {counter}')
#     counter += 1

# SAME CAN BE DONE WITH "ENUMERATE":
# name = 'Simo'
#
# for idx, char in enumerate(name):
#     print(f'char = {char}, idx = {idx}')


# K = int(input())
# for num1 in range(K, 9):
#     print(num1)



# K = int(input())
# L = int(input())
# M = int(input())
# N = int(input())
#
# valid_changes = 0
#
# for first_digit_1 in range(K, 9):
#     if first_digit_1 % 2 != 0:
#         continue
#
#     for second_digit_1 in range(9, L - 1, -1):
#         if second_digit_1 % 2 == 0:
#             continue
#
#         for first_digit_2 in range(M, 9):
#             if first_digit_2 % 2 != 0:
#                 continue
#
#             for second_digit_2 in range(9, N - 1, -1):
#                 if second_digit_2 % 2 == 0:
#                     continue
#
#                 if first_digit_1 == first_digit_2 and second_digit_1 == second_digit_2:
#                     print("Cannot change the same player.")
#                 else:
#                     print(f"{first_digit_1}{second_digit_1} - {first_digit_2}{second_digit_2}")
                    # valid_changes += 1
                    # if valid_changes == 6:
                    #     exit()

#
#
#

# K = int(input())
# L = int(input())
# M = int(input())
# N = int(input())
#
# for numK in range(K, 9):
#     for numL in range(9, L - 1, -1):
#         for numM in range(M, 9):
#             for numN in range(9, N - 1, -1):
#                 if numK % 2 != 0 and numM % 2 != 0 and numL % 2 == 0 and numN % 2 == 0:
#                     continue
#                 elif numK == numM and numL == numN:
#                     print("Cannot change the same player.")
#                 else:
#                     print(f"{numK}{numL} - {numM}{numN}")
#


# ---------------------------------------


# CLOCK PROGRAM

# from time import strftime
# from tkinter import *
# from tkinter.ttk import *
#
# root = Tk()
# root.title('Digital SoftUni Clock')
#
# def clock():
#     tick = strftime('%H:%M:%S %p')
#     label.config(text=tick)
#     label.after(1000, clock)
#
# label = Label(root, font=('sans', 100), background='black', foreground='red')
# clock()
# mainloop()

from time import strftime
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Digital SoftUni Clock')

def clock():
    time_str = strftime('%H:%M:%S %p')  # Clearer variable name
    label.config(text=time_str)
    label.after(1000, clock)  # Fixed `after` method

label = Label(root, font=('sans', 100), background='black', foreground='orange')  # Fixed class name
label.pack(anchor='center')  # Ensure the label is displayed

clock()
root.mainloop()  # Use `root.mainloop()` instead of `mainloop()`
