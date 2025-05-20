compartment_capacity = float(input())
loaded_suitcases = 0
current_suitcase = 0

while True:
    command = input()
    if command == "End":
        print("Congratulations! All suitcases are loaded!")
        break

    suitcase_size = float(command)
    current_suitcase += 1

    if current_suitcase % 3 == 0:
        suitcase_size *= 1.1

    if suitcase_size > compartment_capacity:
        print("No more space!")
        break

    compartment_capacity -= suitcase_size
    loaded_suitcases += 1

print(f"Statistic: {loaded_suitcases} suitcases loaded.")
