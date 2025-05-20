# Град 0 ≤ s ≤ 500 500 < s ≤ 1 000 1 000 < s ≤ 10 000 s > 10 000
# Sofia    5%            7%                8%         12%
# Varna    4.5%          7.5%             10%          13%
# Plovdiv   5.5%         8%                12%         14.5%

city_name = input()
sales_amounts = float(input())

comission = 0

ERROR_DATA = False

if city_name == 'Sofia':
    if 0 <= sales_amounts <= 500:
        comission = 5
    elif 500 < sales_amounts <= 1000:
        comission = 7
    elif 1000 < sales_amounts <= 10000:
        comission = 8
    elif sales_amounts > 10000:
        comission = 12
    else:
        ERROR_DATA = True

elif city_name == 'Varna':
    if 0 <= sales_amounts <= 500:
        comission = 4.5
    elif 500 < sales_amounts <= 1000:
        comission = 7.5
    elif 1000 < sales_amounts <= 10000:
        comission = 10
    elif sales_amounts > 10000:
        comission = 13
    else:
        ERROR_DATA = True

elif city_name == 'Plovdiv':
    if 0 <= sales_amounts <= 500:
        comission = 5.5
    elif 500 < sales_amounts <= 1000:
        comission = 8
    elif 1000 < sales_amounts <= 10000:
        comission = 12
    elif sales_amounts > 10000:
        comission = 14.5
    else:
        ERROR_DATA = True

else:
    ERROR_DATA = True

if ERROR_DATA:
    print('error')
else:
    print(f'{(sales_amounts * comission / 100):.2f}')

# ---------------------------------------------------------------
# My initial solution:
# if city_name == 'Sofia':
#     if 0 <= sales_amounts <= 500:
#         comission = 5
#         print(f'{(sales_amounts * comission / 100):.2f}')
#     elif 500 < sales_amounts <= 1000:
#         comission = 7
#         print(f'{(sales_amounts * comission / 100):.2f}')
#     elif 1000 < sales_amounts <= 10000:
#         comission = 8
#         print(f'{(sales_amounts * comission / 100):.2f}')
#     elif sales_amounts > 10000:
#         comission = 12
#         print(f'{(sales_amounts * comission / 100):.2f}')
#
# if city_name == 'Varna':
#     if 0 <= sales_amounts <= 500:
#         comission = 4.5
#         print(f'{(sales_amounts * comission / 100):.2f}')
#     elif 500 < sales_amounts <= 1000:
#         comission = 7.5
#         print(f'{(sales_amounts * comission / 100):.2f}')
#     elif 1000 < sales_amounts <= 10000:
#         comission = 10
#         print(f'{(sales_amounts * comission / 100):.2f}')
#     elif sales_amounts > 10000:
#         comission = 13
#         print(f'{(sales_amounts * comission / 100):.2f}')
#
# if city_name == 'Plovdiv':
#     if 0 <= sales_amounts <= 500:
#         comission = 5.5
#         print(f'{(sales_amounts * comission / 100):.2f}')
#     elif 500 < sales_amounts <= 1000:
#         comission = 8
#         print(f'{(sales_amounts * comission / 100):.2f}')
#     elif 1000 < sales_amounts <= 10000:
#         comission = 12
#         print(f'{(sales_amounts * comission / 100):.2f}')
#     elif sales_amounts > 10000:
#         comission = 14.5
#         print(f'{(sales_amounts * comission / 100):.2f}')
#
# else:
#     print('error')



