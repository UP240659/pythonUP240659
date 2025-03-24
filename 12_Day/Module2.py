import random
import string

# Ejercicio 1: Generación de lista de colores hexadecimales
def lista_de_colores_hexa(num):
    colores_hexa = []
    for _ in range(num):
        color_aleatorio = '#' + ''.join(random.choices('0123456789abcdef', k=6))  # Genera un color aleatorio en formato hexadecimal
        colores_hexa.append(color_aleatorio)
    return colores_hexa

print(lista_de_colores_hexa(3))

# Ejercicio 2: Generación de lista de colores RGB
def lista_de_colores_rgb(num):
    lista_rgb = [] 
    for _ in range(num):
        rojo = random.randint(0, 255)  # Genera un valor aleatorio para el color rojo
        verde = random.randint(0, 255)  # Genera un valor aleatorio para el color verde
        azul = random.randint(0, 255)  # Genera un valor aleatorio para el color azul
        lista_rgb.append(('rgb', rojo, verde, azul))  # Almacena el color en formato RGB
    return lista_rgb

print(lista_de_colores_rgb(4))

# Ejercicio 3: Generación de colores en formato HEXA o RGB
def generar_colores(tipo, num):
    colores = []
    if tipo == 'hexa':  # Si el tipo es hexadecimal
        for _ in range(num):
            color_aleatorio = '#' + ''.join(random.choices('0123456789abcdef', k=6))  # Genera un color aleatorio en formato hexadecimal
            colores.append(color_aleatorio)
        return colores
    elif tipo == 'rgb':  # Si el tipo es RGB
        for _ in range(num):
            rojo = random.randint(0, 255)
            verde = random.randint(0, 255)
            azul = random.randint(0, 255)
            colores.append(('rgb', rojo, verde, azul))  # Almacena el color en formato RGB
        return colores
    else:
        return 'Tipo de color inválido'  # Si el tipo no es válido, devuelve un mensaje de error

print('Generar colores Hexadecimales:', generar_colores('hexa', 3))
print('Generar colores RGB:', generar_colores('rgb', 3))
print(generar_colores('tp', 5))  # Caso con un tipo inválido
