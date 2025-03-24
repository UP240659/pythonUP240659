import random
import string

# Ejercicio 1: Generación de ID de usuario aleatorio
def generar_id_usuario_aleatorio():
    caracteres = string.ascii_letters + string.digits  # Letras y números
    id_usuario_aleatorio = ''.join((random.choice(caracteres)) for _ in range(6))  # Genera un ID de 6 caracteres
    return id_usuario_aleatorio

print('ID de usuario:', generar_id_usuario_aleatorio())

# Ejercicio 2: Generación de ID de usuario por el usuario
def generar_id_usuario_por_usuario():
    caracteres = string.ascii_letters + string.digits  # Letras y números
    num_caracteres = int(input('Ingresa el número de caracteres que quieres en tu usuario:'))  # Número de caracteres
    num_IDs = int(input('¿Cuántas opciones quieres?'))  # Número de ID a generar

    def generar_id_usuario_aleatorio():
        return ''.join((random.choice(caracteres)) for _ in range(num_caracteres))  # Genera un ID aleatorio

    for i in range(num_IDs):  # Genera la cantidad de IDs solicitados
        id_usuario_aleatorio = generar_id_usuario_aleatorio()
        print(f"{id_usuario_aleatorio}")  # Muestra el ID generado

generar_id_usuario_por_usuario()

# Ejercicio 3: Generación de color RGB aleatorio
def generar_color_rgb():
    rojo = random.randint(0, 255)  # Valor aleatorio para el color rojo
    verde = random.randint(0, 255)  # Valor aleatorio para el color verde
    azul = random.randint(0, 255)  # Valor aleatorio para el color azul
    return (rojo, verde, azul)  # Devuelve una tupla con los valores RGB

color_rgb_aleatorio = generar_color_rgb()
print(color_rgb_aleatorio)
