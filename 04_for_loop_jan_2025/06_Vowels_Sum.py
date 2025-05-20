# буква    a e i o u
# стойност 1 2 3 4 5

text = input()

index_sum = 0

for i in range(len(text)):
    if text[i] == 'a':
        index_sum += 1
    if text[i] == 'e':
        index_sum += 2
    if text[i] == 'i':
        index_sum += 3
    if text[i] == 'o':
        index_sum += 4
    if text[i] == 'u':
        index_sum += 5

print(index_sum)

