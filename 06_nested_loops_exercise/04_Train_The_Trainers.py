total_sum = 0
total_judge_score = 0

judges_count = int(input())

command = input() # 'Finish' or current_presentation, e.g. 'Arrays'

while command != 'Finish':
    current_presentation = command

    current_score = 0
    for _ in range(judges_count):
        judge_score = float(input())
        current_score += judge_score

    current_score_avg = current_score / judges_count

    print(f'{current_presentation} - {current_score_avg:.2f}.')

    total_sum += current_score
    total_judge_score += judges_count
    command = input()

total_avg = total_sum / total_judge_score
print(f"Student's final assessment is {total_avg:.2f}.")