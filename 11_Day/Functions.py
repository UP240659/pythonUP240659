import math
import cmath  

# Ejercicio 1
def sumar_dos_numeros(num1, num2):
    total = num1 + num2
    return total
print('El resultado de la suma es:', sumar_dos_numeros(5, 5))

# Ejercicio 2
def area_de_circulo(radio):
    area = radio**2 * math.pi
    return area
print('El área del círculo:', area_de_circulo(5))

# Ejercicio 3
def sumar_todos_los_numeros(*args):
    if all(isinstance(num, (int, float)) for num in args):
        return sum(args)
    else:
        return "Error: Todos los argumentos deben ser números."
print(sumar_todos_los_numeros('La ', 1, 2, 3, 4, 5, 6))
print(sumar_todos_los_numeros(1, 2, 3, 'hola'))

# Ejercicio 4
def convertir_celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit
print('Celsius a Fahrenheit:', convertir_celsius_a_fahrenheit(32))

# Ejercicio 5
def verificar_estacion(mes):
    if (mes == 'Septiembre' or mes == 'Octubre' or mes == 'Noviembre'):
        return 'Otoño'
    elif (mes == 'Diciembre' or mes == 'Enero' or mes == 'Febrero'):
        return 'Invierno'
    elif (mes == 'Marzo' or mes == 'Abril' or mes == 'Mayo'):
        return 'Primavera'
    elif (mes == 'Junio' or mes == 'Julio' or mes == 'Agosto'):
        return 'Verano'
print('La estación es:', verificar_estacion('Agosto'))

# Ejercicio 6
def calcular_pendiente(x1, x2, y1, y2):
    m = (y2 - y1) / (x2 - x1)
    return m
print('Pendiente:', calcular_pendiente(5, 8, 10, 12))

# Ejercicio 7
def resolver_ecuacion_cuadratica(a, b, c):
    if a == 0:
        return "No es una ecuación cuadrática (a debe ser distinto de cero)."
    
    discriminante = b**2 - 4*a*c
    # Soluciones reales
    if discriminante > 0:
        solucion1 = (-b + math.sqrt(discriminante)) / (2 * a)
        solucion2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return solucion1, solucion2
    # Solución única
    elif discriminante == 0:
        solucion1 = (-b / (2 * a))
        return solucion1
    # Soluciones complejas
    else:
        solucion1 = (-b + cmath.sqrt(discriminante)) / (2 * a)
        solucion2 = (-b - cmath.sqrt(discriminante)) / (2 * a)
        return solucion1, solucion2
    
print(resolver_ecuacion_cuadratica(1, -3, 2))

# Ejercicio 8
def imprimir_lista(lst):
    for i in lst:
        print(i)
mi_lista = [1, 2, 3, 4, 5]
imprimir_lista(mi_lista)

# Ejercicio 9
def invertir_lista(arr):
    lista_invertida = []
    for i in range(len(arr)-1, -1, -1):
        lista_invertida.append(arr[i])
    return lista_invertida
mi_lista1 = [1, 2, 3, 4, 5]
print(invertir_lista(mi_lista1))

# Ejercicio 10
def capitalizar_elementos_lista(cap):
    lista_capitalizada = []
    for i in cap:
        lista_capitalizada.append(i.upper())
    return lista_capitalizada
palabras = ['hola', 'adios']
print(capitalizar_elementos_lista(palabras))

# Ejercicio 11
def agregar_item(lst, item):
    lst.append(item)
    return lst
print(agregar_item(mi_lista, 6))

# Ejercicio 12
def eliminar_item(lst, item):
    lst.remove(item)
    return lst
print(eliminar_item(mi_lista1, 1))

# Ejercicio 13
def suma_de_numeros(num):
    total = 0
    for i in range(0, num+1):
        total += i
    return total
print(suma_de_numeros(5))
print(suma_de_numeros(10))
print(suma_de_numeros(100))

# Ejercicio 14
def suma_de_impares(num):
    total = 0
    for i in range(0, num+1):
        if i % 2 != 0:
            total += i
    return total
print('Suma de los números impares:', suma_de_impares(100))

# Ejercicio 15
def suma_de_pares(num):
    return sum(i for i in range(0, num+1, 2))
print('Suma de los números pares:', suma_de_pares(100))
