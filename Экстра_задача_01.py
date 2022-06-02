# Определите функцию, которая принимает римскую цифру в качестве аргумента и возвращает ее значение в виде числового десятичного целого числа. 


print('Примеры римских цифр: "MMXXII","II","XL","XXX"')
str = input('Введите римскую цифру: ')


def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1

def romanToDecimal(str):
    res = 0
    i = 0

    while (i < len(str)):

        # Получение значения символа s [i]
        s1 = value(str[i])
        if (i+1 < len(str)):

            # Получение значения символа s [i + 1]
            s2 = value(str[i+1])

            # Сравнение обоих значений
            if (s1 >= s2):

                # Значение текущего символа больше или равно следующему символу

                res = res + s1
                i = i + 1

            else:

                # Значение текущего символа больше или равно следующему символу

                res = res + s2 - s1
                i = i + 2

        else:

            res = res + s1
            i = i + 1

    return res
  
print("В десятичном виде это будет")

print(romanToDecimal(str)) 