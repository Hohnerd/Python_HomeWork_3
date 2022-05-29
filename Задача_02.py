# Вычислить число Пи c заданной точностью d. Пример: при d = 0.001,  c= 3.141. 

# Вычисление числа Пи (изначальное)
my_pi = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(15))
# Число Пи с учётом количества знаков после запятой
def CalculatePi(roundVal):
		somepi = round(my_pi,roundVal);
		pi = str(somepi)
		someList = list(pi)
		return somepi;
roundTo = input('Введите количество цифр после запятой для числа Пи: ')
roundint = int(roundTo);
print('Изначальное число Пи: ',my_pi)
print('Число Пи с учётом количества знаков после запятой:',CalculatePi(roundint))