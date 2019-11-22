import matplotlib.pyplot as plt
import numpy as np


def read_coordinates():  # this function reads data of unknowing function
    lines = []
    coord = open('unknowing_function.txt')
    line = coord.read()
    linesInCoord = line.split('\n')

    for i in linesInCoord:
        x, y = i.split('/')
        if x == "x" and y == "y":
            continue
        lines.append((float(x), float(y)))
    lines.sort()
    x = []
    y = []
    for line in lines:
        x.append(line[0])
        y.append(line[1])
    return x, y


def tridiagonal_matrix(main_diagonal, up_diagonal, under_diagonal, values):  # This function found values of roots L
    sigma = []
    alpha = []
    betta = []
    roots = []

    l = len(main_diagonal) - 1
    # y = 0 ----------------------------- i don''d understand this still
    a = 0
    b = 0
    x = 0
    for i in range(len(main_diagonal)):
        y = main_diagonal[i] + under_diagonal[i] * a
        a = -1 * up_diagonal[i] / y
        b = (values[i] - under_diagonal[i] * b) / y

        sigma.append(y)
        alpha.append(a)
        betta.append(b)

    while l >= 0:
        x = alpha[l] * x + betta[l]
        roots.append(x)
        l -= 1

    roots.reverse()
    roots.append(0)
    return roots


def create_matrix(values_x, values_y):  # This function create a new tridiagonal matrix
    main_diagonal = []
    up_diagonal = []
    under_diagonal = [0]
    values = []
    ttt = []
    d = 0

    for i in range(len(values_x) - 1):
        c = 1 / (values_x[i + 1] - values_x[i])
        a = under_diagonal[i]
        b = 2 * (a + c)
        t = (values_y[i + 1] - values_y[i]) * c
        value = 3 * (d + t * c)
        d = t

        under_diagonal.append(c)
        up_diagonal.append(c)
        main_diagonal.append(b)
        ttt.append(t)
        values.append(value)

    up_diagonal.append(0)
    main_diagonal.append(2 * (up_diagonal[-1] + under_diagonal[-1]))
    values.append(3 * ttt[-1] * under_diagonal[-1])
    ttt.append(0)

    return main_diagonal, up_diagonal, under_diagonal, values, ttt


def found_coef(values_y, roots, up_diagonal, ttt):  # This function founds coefficients of polynomial
    coef_a = []
    coef_b = []
    coef_c = []
    coef_d = []

    for i in range(len(up_diagonal) - 1):
        a = values_y[i]
        b = roots[i]
        c = up_diagonal[i] * (3 * ttt[i] - 2 * roots[i] - roots[i + 1])
        d = up_diagonal[i] ** 2 * (-2 * ttt[i] + roots[i] + roots[i + 1])

        coef_a.append(a)
        coef_b.append(b)
        coef_c.append(c)
        coef_d.append(d)

    return coef_a, coef_b, coef_c, coef_d


def polynomial(a, b, c, d, values_x, x):
    polynomial = []
    j = 0
    i = 0

    while j <= len(values_x) - 1 and i <= len(x) - 1:
        if x[i] <= values_x[j + 1]:
            xx = x[i] - values_x[j]
            p = a[j] + xx * (b[j] + xx * (c[j] + xx * d[j]))
            i += 1

            polynomial.append(p)
        else:
            j += 1

    return polynomial

x, y = read_coordinates()
m, u, un, v, t = create_matrix(x, y)
roots = tridiagonal_matrix(m, u, un, v)
a, b, c, d = found_coef(y, roots, u, t)

new_x = []
x0 = x[0]
while x0 <= x[-1]:
    new_x.append(x0)
    x0 += 0.1
new_y = polynomial(a, b, c, d, x, new_x)

plt.plot(x, y, 'o', new_x, new_y, '-')
plt.show()