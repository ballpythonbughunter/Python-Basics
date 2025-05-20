#Напишете програма, която изчислява колко часа ще са необходими на един архитект, за да изготви проектите на
# няколко строителни обекта. Изготвянето на един проект отнема три часа.

#1. Името на архитекта - текст
#2. Брой на проектите, които трябва да изготви - цяло число в интервала [0 … 100]

name_of_architect = input()
number_of_projects = int(input())

consumed_time = number_of_projects * 3

print(f"The architect {name_of_architect} will need {consumed_time} hours to complete {number_of_projects} project/s.")