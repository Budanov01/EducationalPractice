import matplotlib.pyplot as plt
import random
import math
from scipy import stats


# равномерное распределение методом обратных функций !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def inverse_functions_method(N):
    try:
        a, b = input('введите отрезок для нормального распределения методом обратных функций\n'
                     'a, b = ').split(', ')
        a, b = float(a), float(b)
    except Exception:
        print('Возможно вы ввелин что-то не так')
    x1 = []  # массив для хранения значений случайной величины X
    theor_x1 = []  # массив x для построения графика/гистограмы плотности/функции распределения
    theor_y1 = []  # массив y для построения графика плотности
    theor_Fx1 = []  # массив F[x] для построения графика функции распределения
    # цикл нахождения значения случайной величины
    for i in range(N):
        x1.append(random.random() * (b - a) + a)
    x1.sort()
    # заполняем массивы x, y, F[x]
    left = a
    dx = (b - a) / 1000
    while left <= b:
        theor_x1.append(left)
        left += dx
    # f_x - теоретическая плотность вероятвости
    f_x = 1 / (b - a)
    for x in theor_x1:
        theor_y1.append(f_x)
        theor_Fx1.append(f_x * (x - a))
    #   нахождение теоретических и расчетных мат ожиданий и дисперсий !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    sum = 0
    sum1 = 0
    for x in x1:  # находим расчетное мат ожидание
        sum += x
    exp_m_x = sum / N
    for x in x1:  # находим расчетную дисперсию (именованна как sigma)
        x -= exp_m_x
        sum1 += (x ** 2)
    exp_sigma = sum1 / N
    theor_m_x = (b + a) / 2  # теоретическое мат ожидание
    theor_sigma = ((b - a) ** 2) / 12  # теоретическая дисперсия (просто именована как sigma)

    return x1, exp_m_x, exp_sigma, theor_m_x, theor_sigma, theor_x1, theor_y1, theor_Fx1


# распределение Релея методом Неймана!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def Rayleigh_distribution(N):
    try:
        sigma, a, b = input('для распределения Релея методом Неймана\n'
                            'введите ср. кв. отклонения и отрезок [a,b]\n'
                            'sigma ∈ [a, b]; f(x)=max, x=sigma\n'
                            'sigma, a, b = ').split(', ')
        sigma, a, b = float(sigma), float(a), float(b)
    except Exception:
        print('Возможно вы ввелин что-то не так')
    M = 1 / math.e ** ((sigma ** 2) / 2)  # M - максимальное значение плотности распределения
    x2 = []  # массив для хранения значений случайной величины X
    theor_x2 = []  # массив x для построения графика/гистограмы плотности/функции распределения
    theor_y2 = []  # массив y для построения графика плотности
    theor_Fx2 = []  # массив F[x] для построения графика функции распределения
    # цикл нахождения значения случайной величины
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
        else:
            i += 0
    x2.sort()
    # заполняем массивы x, y, F[x]
    left = a
    dx = (b - a) / 1000
    while left <= b:
        theor_x2.append(left)
        left += dx
    for x in theor_x2:
        theor_y2.append((x / sig) * math.e ** (
                (-1 * x ** 2) / (2 * sig)))  # эта ужасная формула - теоретическая плотность распределения
        theor_Fx2.append(
            1 - math.e ** ((-1 * x ** 2) / (2 * sig)))  # эта ужасная формула теоретическая Функция распределения
    #   расчет теоретических и экспериментальных мат ожиданий и дисперсий !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    sum = 0
    sum1 = 0
    for x in x2:  # находим расчетное мат ожидание
        sum += x
    exp_m_x = sum / N
    for x in x2:  # находим расчетную дисперсию
        x -= exp_m_x
        sum1 += (x ** 2)
    exp_sigma = sum1 / N
    theor_m_x = math.sqrt(math.pi / 2) * sigma  # находим теоретическое мат ожидание
    dispersion = (2 - math.pi / 2) * sig  # наодим теоретическую дисперсию

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
    x3 = []  # массив для хранения значений случайной величины X
    theor_x3 = []  # массив x для построения графика/гистограмы плотности/функции распределения
    theor_y3 = []  # массив y для построения графика плотности
    Fx3 = []

    m0 = baseNum / 2  # мат ожидание нормального распределения
    sigma0 = math.sqrt(baseNum / 12)  # сигма нормального распределения
    # находим значения случайной величины X
    for j in range(N):
        v0 = 0  # сумма 6 или 12 случайных чисел от 0 до 1
        for i in range(baseNum):
            v0 += random.random()
        epsilon = (v0 - m0) / sigma0
        x = sigma * epsilon + m  # 1 значение случайной величины
        x3.append(x)
    x3.sort()
    # заполняем массивы x, y
    a = x3[0]
    b = x3[-1]
    left = a
    dx = (b - a) / 1000
    while left <= b:
        theor_x3.append(left)
        left += dx
    c = 1 / (sigma * math.sqrt(2 * math.pi))  # посчитал раз чтобы не использовать каждый раз цикле A
    sig = sigma ** 2  # посчитал раз чтобы потом не считать много раз
    for x in theor_x3:  # цмкл A :)
        theor_y3.append(c * math.e ** (-1 * (((x - m) ** 2) / (2 * sig))))
        z = (x - m) / sigma
        Fx3.append(stats.norm.cdf(z))
    #   расчет теоретических и экспериментальных мат ожиданий и дисперсий !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    sum = 0
    sum1 = 0
    for x in x3:  # находи расчетное мат ожидание
        sum += x
    exp_m_x = sum / N
    for x in x3:  # находим расчетную дисперсию
        x -= exp_m_x
        sum1 += (x ** 2)
    exp_dispersion = sum1 / N
    # теоретические мат ожидание и ср. кв. отклонение мы вводим сами, потом считаем дисперсию как квадрат сигмы
    return x3, exp_m_x, exp_dispersion, m, sig, theor_x3, theor_y3, Fx3


# функция для сборки расчетной функции распределения
def histogram(x, K, N):
    intervals = []  # массив x для гистограммы функции распределения
    hit = []  # массив в котором храняться кол-во значений случайной величины попавших в определенный интервал
    theta = [0]  # массив частот
    Fq = []  # массив значений расчетной функции распределения

    dx = (x[-1] - x[0]) / K
    left = x[0]
    # заполняем массив x для гистограммы функции распределения
    for i in range(K + 1):
        intervals.append(left + dx * i)
    # подсчитываем кол-во попавших значений случайной величины в определенный отезок
    i = 0
    for j in range(len(intervals) - 1):
        k = 0  # кол-во попавших значений
        while x[i] < intervals[j + 1]:
            k += 1
            i += 1
        hit.append(k)
    hit[-1] += 1
    # находим частоту
    for i in range(len(hit)):
        theta_i = hit[i] / N
        theta.append(theta_i)
    # находим значение расчетной функии распределения как сумму частот
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
    x3, m_x3, dispersion3, theor_m_x3, theor_dispersion3, new_x3, new_y3, Fx3 = Gaussian_distribution(N)
    intervals3, f3 = histogram(x3, K, N)
    #   график/гистограмма плотности распределения
    axs1.hist(x3, K, density=1)
    axs1.plot(new_x3, new_y3, 'r-')
    axs1.set_title('Гаусово р-е, частота')
    #   график/полигон функции распределения
    axs2.step(intervals3, f3)
    axs2.plot(new_x3, Fx3)
    axs2.set_title('Гаусово р-е, выб-я вер-ть')
    print('расчетные данные: M[x]=' + str(round(m_x3, 3)) + ', D[x]=' + str(round(dispersion3, 3)) + '\n'
          + 'теоретические д-е: M[x]=' + str(round(theor_m_x3, 3)) + ', D[x]=' + str(round(theor_dispersion3, 3)))
    plt.show()
else:
    print('Возможно вы неправильно выбрали метод.')