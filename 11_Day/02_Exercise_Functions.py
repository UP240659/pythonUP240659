import statistics
from collections import Counter

# Ejercicio 1
def evens_and_odds(r):
    evens = r // 2 + 1  # Los números pares son la mitad más uno si r es par
    odds = r // 2       # Los números impares son el resto
    if r % 2 != 0:       # Si r es impar, incrementamos los impares por uno
        odds += 1
    return evens, odds
print(evens_and_odds(100))

# Ejercicio 2
def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))
print(factorial(0))

# Ejercicio 3
def is_empty(value):
    return not bool(value)
print(is_empty([]))
print(is_empty('Hola'))

# Ejercicio 4
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def calculate_mean(v):
    return sum(v) / len(v)

def calculate_median(v):
    v_sorted = sorted(v)  # Asegurarse de que la lista esté ordenada
    middle = len(v_sorted) // 2
    if len(v_sorted) % 2 == 0:
        return (v_sorted[middle - 1] + v_sorted[middle]) / 2
    else:
        return v_sorted[middle]

def calculate_mode(v):
    # Usamos Counter para contar las frecuencias de los números
    frequency = Counter(v)
    max_count = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_count]
    return modes

def calculate_range(v):
    return max(v) - min(v)

def calculate_variance(v):
    mean = calculate_mean(v)
    return sum((i - mean) ** 2 for i in v) / len(v)

def calculate_std(v):
    return calculate_variance(v) ** 0.5

# Mostrar resultados
print('Mean:', calculate_mean(values))
print('Median:', calculate_median(values))
print('Mode:', calculate_mode(values))
print('Range:', calculate_range(values))
print('Variance:', calculate_variance(values))
print('Standard Deviation:', calculate_std(values))
