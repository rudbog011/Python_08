print('Введите последовательность чисел:')
count_p = 0
count_m = 0
n = int(input())
while n != 0:
    if n > 0:
        count_p += 1
    elif n < 0:
        count_m += 1
    n = int(input())
print(count_m * count_p)
