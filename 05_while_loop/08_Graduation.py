
name = input()
years_counter = 0
fail_counter = 0
grades_counter = 0

while True:
    annual_grade = float(input())
    years_counter += 1

    if annual_grade < 4:
        fail_counter += 1
        if fail_counter > 1:
            print(f"{name} has been excluded at {years_counter} grade")
            break
        years_counter -= 1
        continue

    grades_counter += annual_grade

    if years_counter == 12:
        average_grade = grades_counter / 12
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break






