#Ако фигурата е квадрат (square): на следващия ред се чете едно дробно число - дължина на страната му
#· Ако фигурата е правоъгълник (rectangle): на следващите два реда четат две дробни числа - дължините на страните му
#· Ако фигурата е кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга
# Ако фигурата е триъгълник (triangle): на следващите два реда четат две дробни числа - дължината на страната му и дължината на височината към нея
#Резултатът да се закръгли до 3 цифри след десетичната запетая.

figure = input()
if figure == 'square':
    square_side = float(input())
    square_area = square_side ** 2
    print(f'{square_area:.3f}')

elif figure == 'rectangle':
    rectangle_side_a = float(input())
    rectangle_side_b = float(input())
    rectangle_area = rectangle_side_a * rectangle_side_b
    print(f'{rectangle_area:.3f}')

elif figure == 'circle':
    circle_radius = float(input())
    from math import pi
    circle_area = pi * (circle_radius ** 2)
    print(f'{circle_area:.3f}')

elif figure == 'triangle':
    triangle_side = float(input())
    triangle_height = float(input())
    triangle_area = triangle_side * triangle_height / 2
    print(f'{triangle_area:.3f}')

