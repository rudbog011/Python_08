print('Введите натуральное число a:')
a = int(input())
a1 = a
s = 0
while a1 > 0:
    s += a1 % 10
    a1 = a1 // 10
if a % s == 0:
    print('YES')
else:
    print('NO')