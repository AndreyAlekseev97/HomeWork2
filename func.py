def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for k in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

n = int(input('Кол-во строк матрицы: '))
m = int(input('Кол-во столбцов матрицы: '))
value = input(f'Значение матрицы: ')
print('-------' * m)
matrix = get_matrix(n,m, value)

if n <= 0:
    print('Неверное кол-во строк ', n)
elif m <= 0:
    print('Неверное кол-во столбцов ', m)
else:
    print('Результат матрицы')
    for i in matrix:
        print(*i)
