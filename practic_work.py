def trap(number):
    password = ''
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                password += str(i) +str(j)
    return password
n = int(input('Введите число от 3 до 20: '))

result = trap(n)
print("Пароль: ", result)


