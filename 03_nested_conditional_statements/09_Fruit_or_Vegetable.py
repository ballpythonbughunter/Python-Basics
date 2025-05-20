# Да се напише програма, която чете име на продукт, въведено от потребителя, и проверява дали е плод или зеленчук.
# · Плодовете "fruit" имат следните възможни стойности: banana, apple, kiwi, cherry, lemon и grapes;
# · Зеленчуците "vegetable" имат следните възможни стойности: tomato, cucumber, pepper и carrot;
# · Всички останали са "unknown".
# Да се изведе "fruit", "vegetable" или "unknown" според въведения продукт.
# banana fruit apple fruit tomato vegetable water unknown

# product_name = input()
#
# if product_name in ('banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes'):
#     print('fruit')
#
# elif product_name in ['tomato', 'cucumber', 'pepper', 'carrot']:
#     print('vegetable')
#
# else:
#     print('unknown')

product_name = input()

if product_name == 'banana' or product_name == 'apple' or product_name == 'kiwi' or product_name == 'cherry' or product_name == 'lemon' or product_name == 'grapes':
    print('fruit')

elif product_name == 'tomato' or product_name == 'cucumber' or product_name == 'pepper' or product_name == 'carrot':
    print('vegetable')

else:
    print('unknown')