# Студент трябва да отиде на изпит в определен час (например в 9:30 часа). Той идва в изпитната зала в даден час на пристигане (например 9:40). Счита се, че студентът е дошъл навреме,
# ако е пристигнал в часа на изпита или до половин час преди това. Ако е пристигнал по-рано повече от 30 минути, той е подранил. Ако е дошъл след часа на изпита, той е закъснял.
# Напишете програма, която прочита време на изпит и време на пристигане и отпечатва дали студентът е дошъл навреме, дали е подранил или е закъснял и с колко часа или минути е подранил или закъснял.

# · Първият ред съдържа час на изпита - цяло число от 0 до 23;· Вторият ред съдържа минута на изпита - цяло число от 0 до 59;· Третият ред съдържа час на пристигане - цяло число от 0 до 23;
# · Четвъртият ред съдържа минута на пристигане - цяло число от 0 до 59.

# · "Late", ако студентът пристига по-късно от часа на изпита;
# · "On time", ако студентът пристига точно в часа на изпита или до 30 минути по-рано;
# · "Early", ако студентът пристига повече от 30 минути преди часа на изпита.
# Ако студентът пристига с поне минута разлика от часа на изпита, отпечатайте на следващия ред:

# · "mm minutes before the start" за идване по-рано с по-малко от час;
# · "hh:mm hours before the start" за подраняване с 1 час или повече. Минутите винаги печатайте с 2 цифри, например "1:05”;
# · "mm minutes after the start" за закъснение под час;
# · "hh:mm hours after the start" за закъснение от 1 час или повече. Минутите винаги печатайте с 2 цифри, например "1:03”.

exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute
time_difference = exam_time - arrival_time
late_time_difference = arrival_time - exam_time



if time_difference > 30:
    print('Early')
    if abs(time_difference) >= 60:
        print(f"{time_difference // 60}:{(time_difference % 60):02d} hours before the start")
    elif time_difference < 60:
        print(f"{time_difference:02d} minutes before the start")

elif time_difference == 0:
    print('On time')

elif 0 < time_difference <= 30:
    print('On time')
    print(f"{time_difference} minutes before the start")

else:
    print('Late')
    if late_time_difference >= 60:
        print(f"{late_time_difference // 60}:{(late_time_difference % 60):02d} hours after the start")
    elif 0 < late_time_difference < 60:
        print(f"{late_time_difference} minutes after the start")








#
# if time_difference > 30:
#     print('Early')
#     if abs(time_difference) >= 60:
#         print(f"{time_difference // 60}:{(time_difference % 60):02d} hours before the start")
#     elif abs(time_difference) < 60:
#         print(f"{abs(time_difference):02d} minutes before the start")




# exam_hour = int(input())
# exam_minute = int(input())
# arrival_hour = int(input())
# arrival_minute = int(input())
#
# hour = 0
# minutes = 0
#
# if ((exam_hour == arrival_hour and exam_minute < arrival_minute) or (exam_hour < arrival_hour and \
#     exam_minute == arrival_minute) or (exam_hour < arrival_hour and exam_minute < arrival_minute) or \
#         (exam_hour < arrival_hour and exam_minute > arrival_minute)):
#     print("Late")
#     if ((arrival_hour - exam_hour == 1) and (arrival_minute - exam_minute < 0)):
#         minutes = (60 - exam_minute) + arrival_minute
#         print(f"{minutes} minutes after the start")
#     elif ((exam_hour == arrival_hour) and (exam_minute < arrival_minute)):
#         minutes = arrival_minute - exam_minute
#         print(f"{minutes} minutes after the start")
#     elif (exam_hour < arrival_hour):
#         hour = arrival_hour - exam_hour
#         if (exam_minute - arrival_minute < 0):
#             minutes = (60 - arrival_minute) + exam_minute
#         else:
#             minutes = exam_minute - arrival_minute
#         print(f"{hour}:{minutes:02d} hours after the start")
#
# elif (exam_hour == arrival_hour and exam_minute == arrival_minute) or ((arrival_hour == (exam_hour - 1)) and \
#     (abs(exam_minute - arrival_minute) >= 30)):
#     print("On time")
#     if ((exam_hour - arrival_hour == 1) and (exam_minute - arrival_minute < 0)):
#         minutes = (60 - arrival_minute) + exam_minute
#         print(f"{minutes} minutes before the start")
#     elif ((exam_hour == arrival_hour) and (exam_minute > arrival_minute)):
#         minutes = exam_minute - arrival_minute
#         print(f"{minutes} minutes before the start")
#     elif (exam_hour > arrival_hour):
#         hour = exam_hour - arrival_hour
#         if (exam_minute - arrival_minute < 0):
#             minutes = (60 - arrival_minute) + exam_minute
#         else:
#             minutes = exam_minute - arrival_minute
#         print(f"{hour}:{minutes:02d} hours before the start")
#
#
# elif (exam_hour == arrival_hour and (exam_minute - arrival_minute > 30)) or (exam_hour > arrival_hour):
#     print('Early')
#     # if (exam_hour == arrival_hour and arrival_minute < exam_minute) or (exam_hour)
#     if ((exam_hour - arrival_hour == 1) and (exam_minute - arrival_minute < 0)):
#         minutes = (60 - arrival_minute) + exam_minute
#         print(f"{minutes} minutes before the start")
#     elif ((exam_hour == arrival_hour) and (exam_minute > arrival_minute)):
#         minutes = exam_minute - arrival_minute
#         print(f"{minutes} minutes before the start")
#     elif (exam_hour > arrival_hour):
#         hour = exam_hour - arrival_hour
#         if (exam_minute - arrival_minute < 0):
#             minutes = (60 - arrival_minute) + exam_minute
#         else:
#             minutes = exam_minute - arrival_minute
#         print(f"{hour}:{minutes:02d} hours before the start")
#
