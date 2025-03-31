# Ejemplo 1: SyntaxError
# print 'Hola mundo'  # Error: Falta paréntesis
print('Hola mundo')    

# Ejemplo 2: NameError
# print(edad)  # Error: Variable no definida
edad = 25
print(edad)    

# Ejemplo 3: IndexError
numeros = [1, 2, 3, 4, 5]
# print(numeros[5])  # Error: Índice fuera de rango
print(numeros[4])     

# Ejemplo 4: ModuleNotFoundError
# import maths  # Error: No existe 'maths'
import math    

# Ejemplo 5: AttributeError
# print(math.PI)  # Error: 'math' no tiene atributo 'PI'
print(math.pi)   

# Ejemplo 6: KeyError
usuario = {'nombre': 'Juan', 'edad': 30}
# print(usuario['ciudad'])  # Error: Clave incorrecta
print(usuario.get('ciudad', 'No disponible'))  

# Ejemplo 7: TypeError
# print(4 + '3')  # Error: No se puede sumar número y string
print(4 + int('3'))   

# Ejemplo 8: ImportError
# from math import power  # Error: No existe 'power' en 'math'
from math import pow   
print(pow(2, 3))       

# Ejemplo 9: ValueError
# print(int('12a'))  # Error: '12a' no es un número válido
print(int('12'))      

# Ejemplo 10: ZeroDivisionError
# print(1 / 0)  # Error: División por cero
print(1 / 1)    
