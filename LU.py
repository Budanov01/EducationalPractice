matrix_a = [[2, 4, -4, 6],
            [1, 4, 2, 1],
            [3, 8, 1, 1],
            [2, 5, 0, 5]]
matrix_b = [8, -4, -5, 2]
n = len(matrix_a) - 1

# Представление матрицы A в виде произведения нижней треугольной матрицы L на верхнюю треугольную матрицу U

# k = 1
j = 1
while j <= n:
    matrix_a[0][j] = matrix_a[0][j] / matrix_a[0][0]
    j += 1

# k = 2,...,(n-1)
k = 1
while k <= n - 1:
    i = k
    while i <= n:
        m1 = 0
        sum1 = 0
        while m1 <= k-1:
            sum1 += matrix_a[i][m1] * matrix_a[m1][k]
            m1 += 1
        matrix_a[i][k] = matrix_a[i][k] - sum1
        i += 1

    j = k + 1
    while j <= n:
        m2 = 0
        sum2 = 0
        while m2 <= k-1:
            sum2 += matrix_a[k][m2] * matrix_a[m2][j]
            m2 += 1
        matrix_a[k][j] = (matrix_a[k][j] - sum2) / matrix_a[k][k]
        j += 1
    k += 1

# k = n
m3 = 0
sum3 = 0
while m3 <= n-1:
    sum3 += matrix_a[n][m3] * matrix_a[m3][n]
    m3 += 1
matrix_a[n][n] = matrix_a[n][n] - sum3

# Представляем A*X=B в виде L*U*X=B
# Прямая подстановка (подстановка U*X=z и решение матрицы L*z=B)
matrix_b[0] = matrix_b[0] / matrix_a[0][0]
i = 1
while i <= n:
    j = 0
    sum4 = 0
    z = i - 1
    while j <= z:
        sum4 += matrix_a[i][j] * matrix_b[j]
        j += 1
    matrix_b[i] = (matrix_b[i] - sum4) / matrix_a[i][i]
    i += 1
# Обратная подстановка ( решение матрицы U*X=Z)
i = n - 1
while i >= 0:
    j = i + 1
    sum5 = 0
    while j <= n:
        sum5 += matrix_a[i][j] * matrix_b[j]
        j += 1
    matrix_b[i] = matrix_b[i] - sum5
    i -= 1

print('После LU-факторизации получилась матрица A')
for z in matrix_a:
    print(z)

print('Корни уравнения X = '+str(matrix_b))