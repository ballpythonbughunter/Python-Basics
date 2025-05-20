
K = int(input())
L = int(input())
M = int(input())
N = int(input())

changes_counter = 0
flag = False

for numK in range(K, 9):
    if numK % 2 != 0:
        continue
    for numL in range(9, L - 1, -1):
        if numL % 2 == 0:
            continue
        for numM in range(M, 9):
            if numM % 2 != 0:
                continue
            for numN in range(9, N - 1, -1):
                if numN % 2 == 0:
                    continue

                if numK == numM and numL == numN:
                    print("Cannot change the same player.")
                else:
                    print(f"{numK}{numL} - {numM}{numN}")

                    changes_counter += 1
                    if changes_counter >= 6:
                        flag = True
                        break
            if flag:
                break
        if flag:
            break
    if flag:
        break







