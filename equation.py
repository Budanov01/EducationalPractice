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
def function_phi(num, x0, coef_a=0, coef_b=0, coef_c=0):
    if num == 1:
        phi_x1 = coef_a * math.exp(-coef_b * x0)
        phi_x2 = -math.log(x0 / coef_a) / coef_b
        der1 = -coef_a * coef_b * math.exp(-coef_b * x0)
        der2 = -1 / (coef_b * x0)
        if math.fabs(der1) < 1:
            return phi_x1
        elif math.fabs(der2) < 1:
            return phi_x2
        elif math.fabs(der1) < math.fabs(der2):
            return phi_x1
        else:
            return phi_x2
    elif num == 2:
        phi_x1 = (math.log10(coef_a * x0) + coef_c) / coef_b
        phi_x2 = (10 ** (coef_b * x0 - coef_c)) / coef_a
        der1 = 1 / (coef_a * x0)
        der2 = (math.log(10) * coef_b * 10 ** (coef_b * x0 - coef_c)) / coef_a
        if math.fabs(der1) < 1:
            return phi_x1
        elif math.fabs(der2) < 1:
            return phi_x2
        elif math.fabs(der1) < math.fabs(der2):
            return phi_x1
        else:
            return phi_x2
    elif num == 3:
        phi_x1 = 1 / (2 ** x0)
        phi_x2 = -1 / (x0 * math.log(2))
        der1 = -math.log(2) / (2 ** x0)
        der2 = -1 / (x0 * math.log(2))
        if math.fabs(der1) < 1:
            return phi_x1
        elif math.fabs(der2) < 1:
            return phi_x2
        elif math.fabs(der1) < math.fabs(der2):
            return phi_x1
        else:
            return phi_x2
    elif num == 4:
        phi_x1 = -(1 + math.cos(x0)) / 3
        phi_x2 = math.acos(-1 - 3 * x0)
        der1 = math.sin(x0) / 3
        der2 = 1 / (math.sqrt(1 - (-3 * x0 - 1) ** 2))
        if math.fabs(der1) < 1:
            return phi_x1
        elif math.fabs(der2) < 1:
            return phi_x2
        elif math.fabs(der1) < math.fabs(der2):
            return phi_x1
        else:
            return phi_x2


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
def simple_iterations(num, N, epsilon, x0, coef_a=0, coef_b=0, coef_c=0):
    xn = function_phi(num, x0, coef_a, coef_b, coef_c)
    z = 0
    while math.fabs(x0 - xn) > epsilon and z < N:
        z += 1
        x0 = xn
        xn = function_phi(num, x0, coef_a, coef_b, coef_c)

    return xn, z


# Метод Ньютона
def newton_method(num, N, epsilon, x0, coef_a=0, coef_b=0, coef_c=0):
    y, d = function(num, x0, coef_a, coef_b, coef_c)
    xn = x0 - y / d
    z = 0
    while math.fabs(x0 - xn) > epsilon and z < N:
        x0 = xn
        y, d = function(num, xn, coef_a, coef_b, coef_c)
        xn = x0 - y / d

        z += 1

    return x0, z



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
        left, right = input('Введите отрезок на котором искать корни (x > 0) alpha, betta = ').split(', ')
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
    root, num_iteration = simple_iterations(num, iteration, epsilon, x0, a, b, c)
    root1, num_iteration1 = newton_method(num, iteration, epsilon, x0, a, b, c)
    y, d = function(num, root, a, b, c)
    y1, d1 = function(num, root1, a, b, c)
    print('В ходе поиска корня было выполнено '+str(num_iteration)+' итераций для метода простых итераций\n'
            'и '+str(num_iteration1)+' для метода Ньютона')
    print('Метод простых итераций:\nЗначение корня = '+str(root)+'\nЗначение функции = '+str(round(y, 8))+'\n'
            'Метод Ньютона\nЗначение корня = '+str(root1)+'\nЗначение функции = '+str(round(y1, 8)))

except Exception:
    print('В следующий раз будте внимательны при вводе данных')