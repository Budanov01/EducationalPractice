import matplotlib.pyplot as plt
import random
import math


# равномерное распределение методом обратных функций
def inverse_functions_method(N):
    try:
        a, b = input('введите отрезок для нормального распределения методом обратных функций\n'
                     'a, b = ').split(', ')
        a, b = float(a), float(b)
    except Exception:
        print('Возможно вы ввелин что-то не так')
    x1 = []

    for i in range(N):
        x1.append(random.random() * (b - a) + a)
    x1.sort()
    return x1


# распределение релея методом Неймана
def Rayleigh_distribution(N):
    try:
        sigma = input('введите значение ср. кв. отклонения\n'
                      'для распределения Релея методом Неймана\n'
                      'sigma = ')
        sigma = float(sigma)
    except Exception:
        print('Возможно вы ввелин что-то не так')

    M = 1 / (math.sqrt(math.e) * sigma)
    x2 = []

    for i in range(N):
        r = random.random()
        y = r * M
        xj = sigma * math.sqrt(-2 * math.log(r))
        g = xj * math.e ** ((-xj ** 2) / (2 * sigma ** 2))
        if y < g:
            x2.append(xj)

    x2.sort()
    return x2


# Гаусово распределение на основе ЦПТ
def Gaussian_distribution(N):
    try:
        m, sigma, baseNum = input('Введите значения мат. ожидания, ср. кв. отклонения,\n'
                                  'кол-во базовых чисел (обчно 6 или 12)\n'
                                  'для вычисления 1 выборки Гаусово распределения на основе ЦПТ\n'
                                  'm, sigma, r = ').split(', ')
        m, sigma, baseNum = float(m), float(sigma), int(baseNum)
    except Exception:
        print('Возможно вы ввелин что-то не так')
    x3 = []

    m0 = baseNum / 2
    sigma0 = math.sqrt(baseNum / 12)

    for j in range(N):
        v0 = 0
        for i in range(baseNum):
            v0 += random.random()
        epsilon = (v0 - m0) / sigma0
        x = sigma * epsilon + m
        x3.append(x)

    x3.sort()
    return x3


# функция для подготовки к гистограмме, входные параметры - x, K (кол-во столбцов гистограммы)
def histogram(x, K, N):
    intervals = []
    hit = []
    theta = []
    names = []
    Fq = []

    delta_x = (x[-1] - x[0]) / K
    left = x[0]

    for i in range(K + 1):
        intervals.append(left + delta_x * i)

    i = 0
    for j in range(len(intervals) - 1):
        k = 0
        while x[i] < intervals[j + 1]:
            k += 1
            i += 1
        hit.append(k)
    hit[-1] += 1

    for i in range(len(hit)):
        theta_i = hit[i] / N
        theta.append(theta_i)
    for i in range(len(intervals) - 1):
        names.append('d' + str(i + 1))
    f = 0
    for elem in theta:
        f += elem
        Fq.append(f)

    return names, theta, Fq


try:
    N = int(input('Число выборок = '))
    K = int(input('Введите кол-во колонок гистограммы/полигона\n'
                  '(обчно в пределах от 9 до 21) К = '))
    method = int(input('Для выборки равномерного распределения методом обратных функций введите 1,\n'
                       'распределение Релея методом Неймана 2,\n'
                       'Гаусово распределение на основе ЦПТ 3,\n'
                       'method = '))
except Exception:
    print('Будте внимательны при вводе данных.')

fig, (axs1, axs2) = plt.subplots(1, 2, figsize=(18, 6), tight_layout=True)
if method == 1:
    x1 = inverse_functions_method(N)
    names1, theta1, f1 = histogram(x1, K, N)
    axs1.bar(names1, theta1)
    axs1.set_title('р-е распределение, частота')
    axs2.step(names1, f1)
    axs2.set_title('р-е распределение, выб-я вер-ть')
    fig
    plt.show()
elif method == 2:
    x2 = Rayleigh_distribution(N)
    names2, theta2, f2 = histogram(x2, K, N)
    axs1.bar(names2, theta2)
    axs1.set_title('р-е Релея, частота')
    axs2.step(names2, f2)
    axs2.set_title('р-е Релея, выб-я вер-ть')
    plt.show()
elif method == 3:
    x3 = Gaussian_distribution(N)
    names3, theta3, f3 = histogram(x3, K, N)
    axs1.bar(names3, theta3)
    axs1.set_title('Гаусово р-е, частота')
    axs2.step(names3, f3)
    axs2.set_title('Гаусово р-е, выб-я вер-ть')
    plt.show()
else:
    print('Возможно вы неправильно выбрали метод.')
