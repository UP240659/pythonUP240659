import random

# Ejercicio 1: Mezclar una lista de manera aleatoria
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def mezclar_lista(lst):
    r_lst = lst[:]
    random.shuffle(r_lst)
    return r_lst

print('Lista original:', valores)
print('Lista aleatoria:', mezclar_lista(valores))

# Ejercicio 2: Generar una lista de 7 números aleatorios únicos
def numero_aleatorio():
    lst_numero_aleatorio = set()
    while len(lst_numero_aleatorio) < 7:
        numero_aleatorio = random.randint(1, 9)  # Usar randint para generar números enteros entre 1 y 9
        lst_numero_aleatorio.add(numero_aleatorio)
    return list(lst_numero_aleatorio)

print(numero_aleatorio())

