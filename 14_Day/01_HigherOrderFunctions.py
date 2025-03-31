from functools import reduce

# Ejercicio 1
paises = ['Estonia', 'Finlandia', 'Suecia', 'Dinamarca', 'Noruega', 'Islandia']
paises_mayusculas = list(map(str.upper, paises))
print(paises_mayusculas)

# Ejercicio 2
numeros = [1, 2, 3, 4, 5]
numeros_cuadrados = list(map(lambda x: x**2, numeros))
print(numeros_cuadrados)

# Ejercicio 3
nombres = ['Asabeneh', 'David', 'Donald', 'Bill']
nombres_mayusculas = list(map(str.upper, nombres))
print(nombres_mayusculas)

# Ejercicio 4
paises_con_land = list(filter(lambda pais: 'land' in pais.lower(), paises))
print(paises_con_land)

# Ejercicio 5
paises_seis_caracteres = list(filter(lambda pais: len(pais) == 6, paises))
print(paises_seis_caracteres)

# Ejercicio 6
paises_mas_seis_caracteres = list(filter(lambda pais: len(pais) >= 6, paises))
print(paises_mas_seis_caracteres)

# Ejercicio 7
paises_comienzan_e = list(filter(lambda pais: pais.startswith('E'), paises))
print(paises_comienzan_e)

# Ejercicio 8
resultado_encadenado = list(map(str.upper, filter(lambda pais: 'land' in pais.lower(), paises)))
print(resultado_encadenado)

# Ejercicio 9
def obtener_lista_strings(lista):
    return list(filter(lambda x: isinstance(x, str), lista))

ejemplo_lista = [1, 'hola', 3.5, 'mundo', True]
print(obtener_lista_strings(ejemplo_lista))

# Ejercicio 10
suma_numeros = reduce(lambda x, y: x + y, numeros)
print(suma_numeros)

# Ejercicio 11
oracion_paises = reduce(lambda x, y: x + ', ' + y, paises[:-1]) + ' y ' + paises[-1] + ' son países del norte de Europa.'
print(oracion_paises)

# Ejercicio 12
def categorizar_paises(paises, patron):
    return list(filter(lambda pais: patron in pais.lower(), paises))

print(categorizar_paises(paises, 'land'))

# Ejercicio 13
def contar_paises_por_letra(paises):
    diccionario = {}
    for pais in paises:
        inicial = pais[0]
        diccionario[inicial] = diccionario.get(inicial, 0) + 1
    return diccionario

print(contar_paises_por_letra(paises))

# Ejercicio 14
def obtener_primeros_diez(paises):
    return paises[:10]

print(obtener_primeros_diez(paises))

# Ejercicio 15
def obtener_ultimos_diez(paises):
    return paises[-10:]

print(obtener_ultimos_diez(paises))
