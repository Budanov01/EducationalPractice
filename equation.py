import sys
import math
import matplotlib.pyplot as plt


# В этой функциии вычисляется значение нужной нам функции и ее производная
# Принимает одно значение номер выбранной функции, коэффициенты a, b и возвращет значение функции в точке
def function(num, x, coef_a=0, coef_b=0, coef_c=0):
    if num == 1:
        exponent = math.exp(-coef_b * x)
        y = coef_a * exponent - x
        derivative = -coef_a * coef_b * exponent - 1
        return y, derivative
    elif num == 2:
        arg = coef_a * x
        lg = math.log10(arg)
        y = lg - coef_b * x + coef_c
        derivative = -coef_b + 1 / (x * math.log(10))
        return y, derivative
    elif num == 3:
        degree_of_two = 2 ** x
        y = x * degree_of_two - 1
        derivative = degree_of_two * (1 + x * math.log(2))
        return y, derivative
    elif num == 4:
        y = 3 * x + math.cos(x) + 1
        derivative = 3 - math.sin(x)
        return y, derivative


# В этой функции вычисляются значения Xn+1 = Phi(Xn)
# def function_phi(num, x0, coef_a=0, coef_b=0, coef_c=0):
#     if num == 1:
#         if x0 <= 0:
#             exponent = math.exp(-coef_b * x0)
#             first_x = coef_a * exponent
#             return first_x
#         else:
#             exponent = math.exp(-coef_b * x0)
#             first_x = coef_a * exponent
#             arg = (x0 / coef_a)
#             second_x = (-1 / coef_b) * math.log(arg)
#             derivative_first = -coef_a * coef_b * exponent
#             derivative_second = -1 / (coef_b * x0)
#             if derivative_first < 1:
#                 return first_x
#             elif derivative_second < 1:
#                 return second_x
#             elif derivative_first < derivative_second:
#                 return first_x
#     elif num == 2:
#         tan_ax = math.tan(coef_a * x0)
#         first_x = tan_ax / coef_b
#         second_x = math.atan(coef_b * x0) / coef_a
#         derivative_first = coef_a / (coef_b * math.cos(coef_a * x0) ** 2)
#         derivative_second = coef_b / (coef_a * (1 + coef_b * x0))
#         if derivative_first < 1:
#             return first_x
#         elif derivative_second < 1:
#             return second_x
#         elif derivative_first < derivative_second:
#             return first_x
#     elif num == 3:
#         if x0 < 0:
#             degree_of_two = 2 ** x0
#             first_x = 1 / degree_of_two
#             return first_x
#         else:
#             degree_of_two = 2 ** x0
#             first_x = 1 / degree_of_two
#             second_x = -math.log(x0, 2)
#             derivative_first = -math.log(2) / degree_of_two
#             derivative_second = -1 / (x0 * math.log(2))
#             if derivative_first < 1:
#                 return first_x
#             elif derivative_second < 1:
#                 return second_x
#             elif derivative_first < derivative_second:
#                 return first_x
#     elif num == 4:
#         cosine = math.cos(x0)
#         first_x = -(1 + cosine) / 3
#         second_x = math.acos(-1 - 3 * x0)
#         derivative_first = math.sin(x0) / 3
#         derivative_second = 3 / (math.sqrt(1 - (-3*x0 - 1) ** 2))
#         if derivative_first < 1:
#             return first_x
#         elif derivative_second < 1:
#             return second_x
#         elif derivative_first < derivative_second:
#             return first_x


# Эта функция рисуется график выбранной функции для визульного представления
def plotting(num, arr_x, coef_a=0, coef_b=0, coef_c=0):
    arr_y = []
    for xx in arr_x:
        y, d = function(num, xx, coef_a, coef_b, coef_c)
        arr_y.append(y)
    plt.plot(arr_x, arr_y)
    plt.show()


# В этой функции происходит выделение интервалов локализации
def localization(num, a, b, coef_a=0, coef_b=0, coef_c=0):
    dx = 0.01
    new_x = []
    sections = []

    while a < b:
        new_x.append(a)
        a += dx
    new_x.append(b)

    for i in range(len(new_x) - 1):
        left = new_x[i]
        right = new_x[i + 1]
        y1, d1 = function(num, left, coef_a, coef_b, coef_c)
        y2, d2 = function(num, right, coef_a, coef_b, coef_c)
        p = y1 * y2
        if p < 0:
            sections.append([left, right])

    return sections


# нахождение корней методом простых итераций
# def simple_iterations(num, N, epsilon, x0, coef_a=0, coef_b=0, coef_c=0):
#     x1n = x0
#     x1n1 = function_phi(num, x1n, coef_a, coef_b, coef_c)
#     x1n = x1n1
#     z = 2
#     while x1n - x1n1 > epsilon or z <= N:
#         x1n1 = function_phi(num, x1n, coef_a, coef_b, coef_c)
#         x1n = x1n1
#         z += 1
#
#     return x1n


# Метод Ньютона
def newton_method(num, N, epsilon, x0, coef_a, coef_b, coef_c=0):
    xn = x0
    y, d = function(num, xn, coef_a, coef_b, coef_c)
    xn1 = xn - y / d
    z = 1
    while xn1 - xn > epsilon and z < N:
        xn = xn1
        y, d = function(num, xn, coef_a, coef_b, coef_c)
        xn1 = xn - y / d

        z += 1

    return xn1, z



try:
    a, b, c = 0, 0, 0
    left, right = 0, 0
    epsilon, iteration = input('Введите погрешность и максимальное число итераций epsilon, N = ').split(', ')
    epsilon, iteration = float(epsilon), int(iteration)
    num = int(input('Выберите уравнение\n'
                    '1) ae^(-bx)-x=0\n'
                    '2) lg(ax)-bx+c=0\n'
                    '3) x2^x=1\n'
                    '4) 3x+cos(x)+1=0\n'
                    '№ = '))
    if num == 1:
        a, b = input('Введите коэффициенты a, b = ').split(', ')
        a, b = float(a), float(b)
        left, right = input('Введите отрезок на котором искать корни alpha, betta = ').split(', ')
        left, right = float(left), float(right)
    if num == 2:
        a, b, c = input('Введите коэффициенты a, b, c = ').split(', ')
        a, b, c = float(a), float(b), float(c)
        left, right = input('Введите отрезок на котором искать корни alpha, betta = ').split(', ')
        left, right = float(left), float(right)
    if num == 3:
        left, right = input('Введите отрезок на котором искать корни alpha, betta = ').split(', ')
        left, right = float(left), float(right)
    if num == 4:
        left, right = input('Введите отрезок на котором искать корни (в градусах) alpha, betta = ').split(', ')
        left, right = math.radians(float(left)), math.radians(float(right))

    left1 = left
    xxx = []
    delx = 0.01
    while left1 < right:
        xxx.append(left1)
        left1 += delx
    xxx.append(right)

    sec = localization(num, left, right, a, b, c)
    plotting(num, xxx, a, b, c)
    if len(sec) == 0:
        print('Извините, но на этом отрезке нет корней.')
        sys.exit()
    print('функция имеет корни в этих интервалах ')
    print(sec)
    x0 = float(input('Введите приближеное значение x0 = '))
    root, num_iteration = newton_method(num, iteration, epsilon, x0, a, b, c)
    y, d = function(num, root, a, b, c)
    print('В ходе поиска корня было выполнено '+str(num_iteration)+' итераций')
    print('Значение корня = '+str(root)+'\nЗначение функции = '+str(round(y, 8)))

except Exception:
    print('В следующий раз будте внимательны при вводе данных')