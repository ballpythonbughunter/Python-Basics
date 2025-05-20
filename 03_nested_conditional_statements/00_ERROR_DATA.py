

number = int(input())
ERROR_DATA = False


if 100 < number < 1000:
    print('OK')
else:
    ERROR_DATA = True

if ERROR_DATA:
    print('error')