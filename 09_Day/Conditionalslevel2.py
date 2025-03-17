cal = int(input('Introduce tu calificación: '))

if(cal >= 90):
    print('Tu calificación es A')
elif(cal >= 70 and cal <= 89):
    print('Tu calificación es B')
elif(cal >= 60 and cal <= 69):
    print('Tu calificación es C')
elif(cal >= 50 and cal <= 59):
    print('Tu calificación es D')
elif(cal >= 0 and cal <= 49):
    print('Tu calificación es F')
else:
    print('No introduje una calificación válida')

# Ejercicio 2

mes = str(input('Introduce el mes: '))

if (mes == 'Septiembre' or mes == 'Octubre' or mes == 'Noviembre'):
    print('La estación es Otoño')
elif(mes == 'Diciembre' or mes == 'Enero' or mes == 'Febrero'):
    print('La estación es Invierno')
elif(mes == 'Marzo' or mes == 'Abril' or mes == 'Mayo'):
    print('La estación es Primavera')
elif(mes == 'Junio' or mes == 'Julio' or mes == 'Agosto'):
    print('La estación es Verano')

# Ejercicio 3
frutas = ['banana', 'naranja', 'mango', 'limón']

fruta = str(input('Introduce una fruta: '))

if ((fruta in frutas) == False):
    frutas.append(fruta)
    print('Lista modificada:', frutas)
else:
    print('Esa fruta ya existe en la lista')
