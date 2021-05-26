print('Введите натуральное число a:')
a = int(input())
count = 0
while a > 0:
    if a % 10 == 5:
        count += 1
    a = a // 10
print('Вхождений числа 5:', count)