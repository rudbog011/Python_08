print('Введите натуральное число a:')
a = int(input())
flag = 0
while a % 2 == 0:
    if a % 2 == 0:
        flag += 1
        a = a / 2
print(int(flag))