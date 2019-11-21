import matplotlib.pyplot as plt
import numpy as np
import copy


class readCoordinates():  # this class reads data
    lines = []
    coord = open('coordinates.txt')
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


def interpolation(coordinate_x):  # this function interpolates f(x) in x
    x = readCoordinates.x
    y = readCoordinates.y
    poly = float(0)
    N = len(x)
    for i in range(N):
        temporary_y = y[i]
        temporary_l = float(1)
        for j in range(N):
            if i != j:
                a = coordinate_x - x[j]
                b = x[i] - x[j]
                l = a / b
                temporary_l *= l
        temporary_y *= temporary_l
        poly += temporary_y
    return poly


def new_coordinates():  # this function returns coordinates of interpolated function
    new_x = list()
    new_y = list()
    a = readCoordinates.x[0]
    b = readCoordinates.x[-1]
    step_x = 10
    delta_x = (abs(a) + abs(b)) / step_x
    for i in range(step_x + 1):
        new_x.append(a)
        a += delta_x
    for x in new_x:
        new_y.append(interpolation(x))
    return new_x, new_y


def appOfFunction():  # this function approximates by method of the least squares
    new_x, new_y = new_coordinates()
    n = len(new_x)
    Ylist = list()  # stores Y of  approximating function
    k = int(3)  # k is the degree of a polynomial

    xy = list(range(k))  # this list stores the value of x*y
    for i in range(k):
        xy[i] = float(0)

    systemOfE = list(range(k))  # this list stores the value of the sum Xi
    for t in range(k):
        systemOfE[t] = list(range(k))
        for e in range(k):
            systemOfE[t][e] = float(0)

    for r in range(n):  # this cycle finds the  sum of Xi
        for i in range(k):
            temporaryX = float(1 * new_x[r])
            for j in range(k):
                if i == 0 and j == 0:
                    systemOfE[i][j] = n
                else:
                    temporarySum = systemOfE[i][j]
                    degree = temporaryX ** (i + j)
                    temporarySum += degree
                    systemOfE[i][j] = temporarySum
            temporaryXY = new_y[r] * (new_x[r] ** i)
            xy[i] += temporaryXY

    det = np.linalg.det(systemOfE)
    coefficients = list()  # coefficients of polynomial
    for i in range(k):  # this cycle finds the coefficients of polynomial
        systemOfE_copy = copy.deepcopy(systemOfE)
        for j in range(k):
            systemOfE_copy[j][i] = xy[j]
        det_a = np.linalg.det(systemOfE_copy)
        coefficients.append(det_a / det)

    for i in range(n):  # this cycle finds approximating function
        y = float(0)
        for j in range(k):
            y += coefficients[j] * (new_x[i] ** j)
        Ylist.append(y)
    print(new_x, new_y)
    return new_x, Ylist


x0, y0 = new_coordinates()
x, y = appOfFunction()
plt.plot(x0, y0, 'o', x, y, '-')
plt.show()
