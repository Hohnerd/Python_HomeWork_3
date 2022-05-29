# Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 

# 1. Создаю текстовый файл с целыми числами
with open('Numbers.txt','a') as data:
    data.write('1 2 3 4 5 9 7 3 2 6 8 34 54 11 99 57 92\n') 

# 2. Читаю текстовый файл
path = 'Numbers.txt'
data = open(path,'r')
for line in data:
    print(line)
data.close()          
    