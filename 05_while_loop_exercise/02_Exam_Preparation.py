# Напишете програма, в която Марин решава задачи от изпити, докато не получи съобщение "Enough" от лектора си. При всяка
# решена задача той получава оценка. Програмата трябва да приключи прочитането на данни при команда "Enough" или ако Марин
# получи определения брой незадоволителни оценки. Незадоволителна е всяка оценка, която е по-малка или равна на 4.
#
# · На първи ред - брой незадоволителни оценки - цяло число;
# · След това многократно се четат по два реда:
# o Име на задача – текст;
# o Оценка - цяло число в интервала [2…6]
#
# · Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:
# o "Average score: {средна оценка}"
# o "Number of problems: {броя на всички задачи}"
# o "Last problem: {името на последната задача}"
# · Ако получи определеният брой незадоволителни оценки:
# o "You need a break, {брой незадоволителни оценки} poor grades."

# number_low_score = int(input())
# exercise_counter = 0
# counter = 0
#
# while True:
#     exercise_name = input()
#     command = input()
#     exercise_counter += 1
#     if command != 'Enough':
#         average_score = int(command) / exercise_counter
#
#     else:
#         last_exercise_name = exercise_name
#         print(f"Average score: {average_score}")
#         print(f"Number of problems: {exercise_counter}")
#         print(f"Last problem: {last_exercise_name}")
#         break
#
#     if int(command) <= 4:
#         counter += 1
#         if counter >= number_low_score:
#             print(f"You need a break, {counter} poor grades.")
#             break

allowed_low_score = int(input())

failed_times = 0
solved_exercises = 0
sum_scores = 0
last_exercise = ''
has_failed = True

while failed_times < allowed_low_score:
    exercise_name = input()
    if exercise_name == 'Enough':
        has_failed = False
        break

    score = int(input())
    if score <= 4:
        failed_times += 1
    sum_scores += score
    solved_exercises += 1
    last_exercise = exercise_name

if has_failed:
    print(f"You need a break, {failed_times} poor grades.")
else:
    print(f"Average score: {sum_scores / solved_exercises:.2f}")
    print(f"Number of problems: {solved_exercises}")
    print(f"Last problem: {last_exercise}")
