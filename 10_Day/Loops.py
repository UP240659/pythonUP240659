# Ejercicio 1
print('Con el ciclo while\n')
contador = 0
while contador <= 10:
    print(contador)
    contador = contador + 1
print('Con el ciclo for\n')
for i in range(0, 11, +1):
    print(i)

# Ejercicio 2
print('Decremento de 0 a 10 con while\n')
contador1 = 10
while contador1 >= 0:
    print(contador1)
    contador1 = contador1 - 1
print('Decremento de 0 a 10 con for \n')
for i1 in range(10, -1, -1):
    print(i1)

# Ejercicio 3
for n in range(0, 8, +1):
    print('#' * n)

# Ejercicio 4
print('\n')
for m in range(0, 8):
    print('#  ' * 8)

# Ejercicio 5
print('\n')
for k in range(0, 11):
    print(k, 'x', k, '=', (k * k))

# Ejercicio 6
print('\n')
lista = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in lista:
    print(item)

# Ejercicio 7
print('\n')
for w in range(0, 101):
    if (w % 2 == 0):
        print(w)

# Ejercicio 8
print('\n')
z = 0
while z <= 100:
    if (z % 2 != 0):
        print(z)
    z += 1
