print('Введите натуральное число n,(n ≥ 10):')
n = int(input())
n_max = 0
n_min = n
if n < 0:
    print('Число меньше 10')
else:
    while n != 0:
        if n_max < n % 10:
            n_max = n % 10
        if n_min > n % 10:
            n_min = n % 10
        n = n // 10
    print('Максимальная цифра равна', n_max)
    print('Минимальная цифра равна', n_min)
