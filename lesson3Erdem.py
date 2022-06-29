'''
'Zadacha 1'
def erdem(x,y):
    return x / y
x = int(input('Введите числитель:'))
y = int(input('Введите знаминатель:'))
if y == 0:
    print('На ноль делить нельзя')
else:
    ab = erdem(x,y)
    print(ab)

'Zadacha 2'
def abc(name, familyname, yearborn, email, telephonenumber):
    return print(name, familyname, yearborn, email, telephonenumber)
a = input('Enter name:')
b = input('Enter family name:')
c = input('Enter year born:')
d = input('Enter email:')
e = input('Enter phone number:')
itog = abc(a,b,c,d,e)

'zadacha 3'
def chisla (a,b,c):
    if a>b and b>c:
        return print(a+b)
    if a>b and b<c:
        return print(a+c)
    else:
        return print(b+c)
h1 = int(input('Enter first argument:'))
h2 = int(input('Enter second argument:'))
h3 = int(input('Enter thirth argument:'))
chisla(h1,h2,h3)

'Zadacha 4'
def stepen (x,y):
    t = []
    b=x
    i=1
    while i < y:
        b = b*x
        i += 1
        t.append(b)
    k = max(t)
    return print(k)
g1 = int(input('Enter first argument:'))
g2 = int(input('Enter second argument:'))
stepen(g1,g2)
'''


