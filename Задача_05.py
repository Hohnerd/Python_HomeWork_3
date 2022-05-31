# Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 


# 1. Создаю текстовый файл с целыми числами
with open('Numbers.txt','w') as data:
    data.write('1 2 3 4 5 9 7 3 2 6 8 34 54 11 99 57 92\n') 
print('')
# 2. Читаю текстовый файл
print('Изначальный текстовый файл: ')    
path = 'Numbers.txt'
data = open(path,'r')
for line in data:
    print(line)   
data.close()  
print('Текстовый файл без чётных чисел: ')
# Преобразую файл содержащий строки с список, и иду циклом for в обратной последовательности 
# чтобы урать чётные числа
m = line.split()
newList = list(map(int,m))  
for i in reversed(newList):
    if i%2==0: newList.remove(i)         
print(newList)
# дописываю в исходный файл числа за исключением чётных
with open('Numbers.txt','a') as data:
    data.write(str(newList)) 
data.close()    

