import math
import matplotlib.pyplot as plt


# В этой функциии вычисляется значение нужной нам функции и ее производная
# Принимает одно значение номер выбранной функции, коэффициенты a, b и возвращет значение функции в точке
def function(num, x, coef_a=0, coef_b=0):
    if num == 1:
        exponent = math.exp(-coef_b * x)
        y = coef_a * exponent - x
        derivative = -coef_a * coef_b * exponent - 1
        return y, derivative
    elif num == 2:
        tan_ax = math.tan(coef_a * x)
        y = tan_ax - coef_b * x
        derivative = (coef_a / (math.cos(coef_a * x) ** 2)) - coef_b
        return y, derivative
    elif num == 3:
        degree_of_two = 2 ** x
        y = x * degree_of_two - 1
        derivative = degree_of_two * (1 + x * math.log(2))
        return y, derivative
    elif num == 4:
        y = 3*x + math.cos(x) + 1
        derivative = 3 - math.sin(x)
        return y, derivative


# В этой функции вычисляются значения Xn+1 = Phi(Xn)
def function_phi(num, x01, x02,  coef_a=0, coef_b=0):
    if num == 1:
        exponent = math.exp(-coef_b * x01)
        first_x = coef_a * exponent
        second_x = (-1 / coef_b) * math.log(x02 / coef_a)
        return first_x, second_x
    elif num == 2:
        tan_ax = math.tan(coef_a * x01)
        first_x = tan_ax / coef_b
        second_x = math.atan(coef_b * x02) / coef_a
        return first_x, second_x
    elif num == 3:
        degree_of_two = 2 ** x01
        first_x = 1 / degree_of_two
        second_x = math.log(1 / x02, 2)
        return first_x, second_x
    elif num == 4:
        cosine = math.cos(x01)
        first_x = -(1 + cosine) / 3
        second_x = math.acos(-1 - 3 * x02)
        return first_x, second_x

# Эта функция рисуется график выбранной функции для визульного представления
def plotting(num, arr_x, coef_a=0, coef_b=0):
    arr_y = []
    for xx in arr_x:
        y, d = function(num, xx, coef_a, coef_b)
        arr_y.append(y)
    plt.plot(arr_x, arr_y)
    plt.show()

# В этой функции происходит выделение интервалов локализации
def localization(num, a, b, coef_a=0, coef_b=0):
    dx = 0.1
    new_x = []
    sections = []

    while a < b:
        new_x.append(a)
        a += dx
    new_x.append(b)

    for i in range(len(new_x) - 1):
        y1, d1 = function(num, new_x[i], coef_a, coef_b)
        y2, d2 = function(num, new_x[i + 1], coef_a, coef_b)
        if y1 * y2 < 0:
            sections.append([new_x[i], new_x[i + 1]])

    print('функция имеет корни в этих интервалах ')
    print(sections)
    return sections


# нахождение корней методом простых итераций
def simple_iterations(num, N, epsilon, x0, coef_a=0, coef_b=0):
    x1n, x2n = x0, x0
    x1n1, x2n1 = function_phi(num, x1n, x2n, coef_a, coef_b)
    x1n, x2n = x1n1, x2n1
    z = 2
    while x1n - x1n1 > epsilon or x2n - x2n1 > epsilon or z <= N:
        x1n1, x2n1 = function_phi(num, x1n, x2n, coef_a, coef_b)
        x1n, x2n = x1n1, x2n1
        z += 1
    y1 = function(num, x1n1, coef_a, coef_b)
    y2 = function(num, x2n1, coef_a, coef_b)
    if y1 < y2:
        return x1n1
    else:
        return x2n1

xxx = []
delx = 0.01
pi = math.pi
a = math.radians(-180)
b = math.radians(180)
while a < b:
    xxx.append(a)
    a += delx
xxx.append(b)

localization(4, -3, b, 4, 6)
plotting(4, xxx, 4, 6)
root = simple_iterations(1, 1000, 0.000001, -0.6, 4, 6)
print(root)
