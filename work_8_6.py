print('Введите последовательность чисел:')
count_n = 0
summa = 0
n = int(input())
while n != 0:
    summa += n
    count_n += 1
    n = int(input())
print(int(summa/count_n))