
"Задача 3"

print('Введите число месяца:')
a = int(input())
b = ['winter', 'spring', 'summer', 'autumn']
if a < 3:
    print(b[0])
if a >= 3:
    if a < 6:
        print(b[1])
if a >= 6:
    if a < 9:
        print(b[2])
if a >= 9:
    if a < 12:
        print(b[3])
if a == 12:
    print(b[0])

"Задача 4"
a = input('Введите предложение:')
a = a.split()
c = ()
i = 0
n = 1
while i <= len(a):
    print(n, '.', a[i] [0:11])
    i += 1
    n += 1
    if i == len(a):
        break

"Задача 5"
my_list = [7,5,3,3,2]
print('Введите новый элемент рейтинга:')
my_list.append(int(input()))
my_list.sort()
my_list.reverse()
print(my_list)


