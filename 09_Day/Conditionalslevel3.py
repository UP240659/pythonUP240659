persona = {
    'primer_nombre': 'Asabeneh',
    'apellido': 'Yetayeh',
    'edad': 250,
    'pais': 'Finlandia',
    'esta_casado': True,
    'habilidades': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'direccion': {
        'calle': 'Space street',
        'codigo_postal': '02210'
    }
}

# Ejercicio 1
if (('habilidades' in persona) == True):
    lista_habilidades = persona['habilidades']

    medio = len(lista_habilidades) // 2
    print('Habilidad del medio:', lista_habilidades[medio])
else:
    print('Habilidades no encontradas')

# Ejercicio 2
if (('Python' in lista_habilidades) == 'True'):
    print('Él tiene la habilidad')
else:
    print('Él no tiene la habilidad')

# Ejercicio 3
if(('JavaScript' in lista_habilidades and 'React' in lista_habilidades)):
    print('Él es un desarrollador front end')
elif(('Node' in lista_habilidades and 'Python' in lista_habilidades and 'MongoDB' in lista_habilidades)):
    print('Él es un desarrollador backend')
elif(('React' in lista_habilidades and 'Node' in lista_habilidades and 'MongoDB' in lista_habilidades)):
    print('Él es un desarrollador fullstack')
else:
    print('Título desconocido')

# Ejercicio 4
casado = str(input('¿Está casado?'))
vive = str(input('¿Dónde vives?'))

if(vive == 'Finlandia' and casado == 'Sí'):
    print('Asabeneh Yetayeh vive en Finlandia. Él está casado.')
else:
    print('ok')
