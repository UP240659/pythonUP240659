#Declarar edad y altura

edad=18
estatura=1.85

#Problemas triangulo

base=int (input('Base del triangulo'))
altura=int (input('Altuta del triangulo'))
print('El area del triangulo es de', base * altura /2)
lado1=int(input('Ingrese el primer lado del triangulo'))
lado2=int(input('Ingrese el segundo lado del triangulo'))
lado3=int(input('Ingrese el tercer lado del triangulo'))
print('El perimetro del triangulo es de',lado1 + lado2 + lado3)

#Problemas Rectangulo 

ladorectangulo1=int (input('Primer lado del rectangulo'))
ladorectangulo2=int (input('Segundo lado del rectangulo'))
print ('EL area del rectangulo es de', ladorectangulo1 * ladorectangulo2)
print ('El perimetro del rectangulo es de ', 2 * ladorectangulo1 + 2 * ladorectangulo2)

#Problemas circulo 

pi=3.14
radio=int (input('Ingrese radio del circulo-'))
print('El area del circulo es', radio * radio * pi)

# Pendiente dada la formula y = 2x -2 ejercicio 8
x1,y1= 0,-2
x2,y2=1,0

print('La pendiente de es de:',(y2-y1)/(x2-x1))
#pendiente con los puntos (3,4) (9,11) 9
x1,y1= 3,4
x2,y2=9,11
print('La pendiente de es de:',(y2-y1)/(x2-x1))

#10 Comparacion de resultados 




#valores de x 11
for x in range (-5,5):
    y = x**2 + 9*x + 9 
    print('el valor de y es: ',x**2 + 9*x + 9 )
    if (y==0):
        print('El valor de y es cero cuando x vale: ', x )
    
#12

palabra1 = 'python'
palabra2 = 'dragon'

longitud1 = len(palabra1)
longitud2 = len(palabra2)

falsy_comparation = longitud1>longitud2
print('El numero de letras de python:',longitud1)
print('El numero de letras de dragon:',longitud2)
print('la comparacion es false porque tienen el mismo numero de letras',falsy_comparation)    

#13

contiene_on = ('on' in palabra1) and ('on' in palabra2)

print('¿se encutra la terminacion en ambas palabras?',contiene_on)

#14
frase= 'I hope this course is not full of jargon'
contiente_jargon =  ('jargon' in frase)

print('¿esta la palabra?',contiente_jargon)

#15


#16
longitud1_float= float(longitud1)
longitud1_str = str(longitud1_float)

print(type(longitud1_float))
print(type(longitud1_str))

#17

numero = int(input('ingrese un numero: '))

if (numero%2==0):
    print('el numero es par')
else:
    print('el numero es impar')

#18

residuo = 7//3
valor_entero = int(2.7)
comparacion= residuo== valor_entero
print('¿La comapracion es verdadera?',comparacion)

#19

valor_int = 10 
valor_str = '10'
comparacion2 = valor_entero==valor_str
print('¿son del mismo tipo?', comparacion2)

#20

valor1 = int(9.8)
valor2 = 10
comparacion3= valor1 == valor2
print('¿Son iguales?',comparacion3)

#21
hours = int(input('ingrese las horas que trabajo:'))
tarifa = float(input('Ingresa la tarifa:'))
pago = hours*tarifa
print('El pago de la semana es de:',pago)

#22
years=int(input('Ingresa el numero de años que ha vivido:'))
print('La cantidad de segundos es de:',31536000*years)
#23

for i in range  (1,6):
    print(f"{i} 1 {i} {i*2} {i*3}")
