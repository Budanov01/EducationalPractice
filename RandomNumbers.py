import matplotlib.pyplot as plt
import random
import math


# равномерное распределение методом обратных функций !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def inverse_functions_method(N):
    try:
        a, b = input('введите отрезок для нормального распределения методом обратных функций\n'
                     'a, b = ').split(', ')
        a, b = float(a), float(b)
    except Exception:
        print('Возможно вы ввелин что-то не так')
    x1 = []
    theor_x1 = []
    theor_y1 = []
    theor_Fx1 = []

    for i in range(N):
        x1.append(random.random() * (b - a) + a)
    x1.sort()

    left = a
    dx = (b - a) / 1000
    while left <= b:
        theor_x1.append(left)
        left += dx
    f_x = 1 / (b - a)
    for x in theor_x1:
        theor_y1.append(f_x)
        theor_Fx1.append(f_x * (x - a))
#   расчет теоретических и экспериментальных мат ожиданий и дисперсий !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    sum = 0
    sum1 = 0
    for x in x1:
        sum += x
    exp_m_x = sum / N
    for x in x1:
        x -= exp_m_x
        sum1 += (x ** 2)
    exp_sigma = sum1 / N
    theor_m_x = (b + a) / 2
    theor_sigma = ((b - a) ** 2) / 12

    return x1, exp_m_x, exp_sigma, theor_m_x, theor_sigma, theor_x1, theor_y1, theor_Fx1


# распределение Релея методом Неймана!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def Rayleigh_distribution(N):
    try:
        a, b, sigma = input('введите значение ср. кв. отклонения\n'
                      'для распределения Релея методом Неймана\n'
                      'sigma = ').split(', ')
        a, b, sigma = float(a), float(b), float(sigma)
    except Exception:
        print('Возможно вы ввелин что-то не так')
    M = 1 / math.e ** ((sigma ** 2) / 2)
    x2 = []
    theor_x2 = []
    theor_y2 = []
    theor_Fx2 = []

    i = 1
    sig = sigma ** 2
    while i <= N:
        r1 = random.random()
        r2 = random.random()
        y = r2 * M
        xj = a + (b - a) * r1
        g = (xj / sig) * math.e ** ((-1 * xj ** 2) / (2 * sigma ** 2))
        if y < g:
            x2.append(xj)
            i += 1
            print('hi')
        else:
            i += 0
    x2.sort()

    left = a
    dx = (b - a) / 1000
    while left <= b:
        theor_x2.append(left)
        left += dx
    for x in theor_x2:
        theor_y2.append((x / sig) * math.e ** ((-1 * x ** 2) / (2 * sig)))
        theor_Fx2.append(1 - math.e ** ((-1 * x ** 2) / (2 * sig)))
#   расчет теоретических и экспериментальных мат ожиданий и дисперсий !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    sum = 0
    sum1 = 0
    for x in x2:
        sum += x
    exp_m_x = sum / N
    for x in x2:
        x -= exp_m_x
        sum1 += (x ** 2)
    exp_sigma = sum1 / N
    theor_m_x = math.sqrt(math.pi / 2) * sigma
    dispersion = (2 - math.pi / 2) * sig

    return x2, exp_m_x, exp_sigma, theor_m_x, dispersion, theor_x2, theor_y2, theor_Fx2


# Гаусово распределение на основе ЦПТ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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
    theor_x3 = []
    theor_y3 = []

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

    a = x3[0]
    b = x3[-1]
    left = a
    dx = (b - a) / 1000
    while left <= b:
        theor_x3.append(left)
        left += dx
    c = 1 / (sigma * math.sqrt(2 * math.pi))
    sig = sigma ** 2
    for x in theor_x3:
        theor_y3.append(c * math.e ** (-1 * (((x - m) ** 2) / (2 * sig))))
#   расчет теоретических и экспериментальных мат ожиданий и дисперсий !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    sum = 0
    sum1 = 0
    for x in x3:
        sum += x
    exp_m_x = sum / N
    for x in x3:
        x -= exp_m_x
        sum1 += (x ** 2)
    exp_dispersion = sum1 / N
    return x3, exp_m_x, exp_dispersion, m, sig, theor_x3, theor_y3


# функция для сборки расчетной функции распределения
def histogram(x, K, N):
    intervals = []
    hit = []
    theta = [0]
    Fq = []

    dx = (x[-1] - x[0]) / K
    left = x[0]

    for i in range(K + 1):
        intervals.append(left + dx * i)

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

    f = 0
    for elem in theta:
        f += elem
        Fq.append(f)

    return intervals, Fq


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
    x1, m_x1, dispersion1, theor_m_x1, theor_dispirsion1, new_x1, new_y1, Fx1 = inverse_functions_method(N)
    intervals1, f1 = histogram(x1, K, N)
    #   график/гистограмма плотности распределения
    axs1.hist(x1, K, density=1)
    axs1.plot(new_x1, new_y1, 'r-')
    axs1.set_title('равномерное р-е, частота')
    #   график/полигон функции распределения
    axs2.step(intervals1, f1)
    axs2.plot(new_x1, Fx1)
    axs2.set_title('р-е распределение, выб-я вер-ть')
    print('расчетные данные: M[x]=' + str(round(m_x1, 3)) + ', D[x]=' + str(round(dispersion1, 3)) + '\n'
          + 'теоретические д-е: M[x]=' + str(round(theor_m_x1, 3)) + ', D[x]=' + str(round(theor_dispirsion1, 3)))
    plt.show()
elif method == 2:
    x2, m_x2, dispersion2, theor_m_x2, theor_dispersion2, new_x2, new_y2, Fx2 = Rayleigh_distribution(N)
    intervals2, f2 = histogram(x2, K, N)
    #   график/гистограмма плотности распределения
    axs1.hist(x2, K, density=1)
    axs1.plot(new_x2, new_y2, 'r-')
    axs1.set_title('р-е Релея, частота')
    #   график/полигон функции распределения
    axs2.step(intervals2, f2)
    axs2.plot(new_x2, Fx2)
    axs2.set_title('р-е Релея, выб-я вер-ть')
    print('расчетные данные: M[x]=' + str(round(m_x2, 3)) + ', D[x]=' + str(round(dispersion2, 3)) + '\n'
          + 'теоретические д-е: M[x]=' + str(round(theor_m_x2, 3)) + ', D[x]=' + str(round(theor_dispersion2, 3)))
    plt.show()
elif method == 3:
    x3, m_x3, dispersion3, theor_m_x3, theor_dispersion3, new_x3, new_y3 = Gaussian_distribution(N)
    intervals3, f3 = histogram(x3, K, N)
    #   график/гистограмма плотности распределения
    axs1.hist(x3, K, density=1)
    axs1.plot(new_x3, new_y3, 'r-')
    axs1.set_title('Гаусово р-е, частота')
    #   график/полигон функции распределения
    axs2.step(intervals3, f3)
    axs2.set_title('Гаусово р-е, выб-я вер-ть')
    print('расчетные данные: M[x]=' + str(round(m_x3, 3)) + ', D[x]=' + str(round(dispersion3, 3)) + '\n'
          + 'теоретические д-е: M[x]=' + str(round(theor_m_x3, 3)) + ', D[x]=' + str(round(theor_dispersion3, 3)))
    plt.show()
else:
    print('Возможно вы неправильно выбрали метод.')
