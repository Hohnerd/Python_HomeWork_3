# Найти НОК двух чисел

a = int(input('Введите число a: '))
b = int(input('Введите число a: '))
i = min(a, b)
while True:
    if i%a==0 and i%b==0:
        break
    i += 1
print('НОК двух введённых чисел =',i)

