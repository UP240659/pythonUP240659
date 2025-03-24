# Ejercicio 1
n = 0
suma = 0
while n <= 100:
    suma = suma + n
    n += 1
print('La suma de todos los números es:', suma)

# Ejercicio 2
print('\n')
k = 0
suma_pares = 0
suma_impares = 0
while k <= 100:
    if (k % 2 != 0):
        suma_impares = suma_impares + k
    elif (k % 2 == 0):
        suma_pares = suma_pares + k
    k += 1
print('La suma de todos los números pares es:', suma_pares, 'Y la suma de todos los números impares es:', suma_impares)
