#1
result = 'Thirty' + ' '+  'Days' + ' '+ 'Of' +' '+ 'Python'
print(result)
#2
result1 = 'Coding' + ' '+  'For' + ' '+ 'all' 
print(result1)
#3
company = 'Coding For All'
print(company) 
#5
print(len(company))
companymayuscula =company.upper()
print(companymayuscula)
#8
companymin =company.lower()
print(companymin)

companycap =company.capitalize()
print(companycap)

companytit =company.title()
print(companytit)

companyswap =company.swapcase()
print(companyswap)

#9

cortar_palabra = " ".join(company.split()[1:])
print (cortar_palabra)

#10

print(company.index('Coding'))

#11

texto = "Coding For All"
new_text = texto.replace("Coding", "Python")
print(new_text)

#12

nuevo_texto = new_text.replace('All','Everyone')
print(nuevo_texto)

#13

print(company.split())

#14

empresas= "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(empresas.split(","))

#15

print(company[0])

#16

print(company[13])

#17

print(company[10])

#18, 19

companyacron = "Python For All"
print('La abreviacion es', companyacron[0], companyacron[7], companyacron[11])

#20 

print (company.index('C'))

#21

print (company.index('F'))

#22

print (company.rfind('i'))

#23

sentence = 'You cannot end a sentence with because because because is a conjunction'
print (sentence.rfind('because'))

#24


print(sentence.rindex('because'))

#25

print(sentence.split('because'))

#26

print(sentence.find('because'))


#27

print(sentence.split('because'))


#28

print(company.startswith('Coding'))

#29

print(company.startswith('coding'))

#30

spaces = '    Coding For All      '
print(spaces.strip())

#31

example1 ='30DaysOfPython'
example2='thirty_days_of_python'
print(example1.isidentifier())
print(example2.isidentifier())

#32

librerias = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
resultado = " # ".join(librerias)
print(resultado)


#33

oracion = "I am enjoying this challenge.\nI just wonder what is next."
print (oracion)


#34

datos = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(datos)


#35

radio = 10
area = 3.14 * radio **2
print('El area del circulo es', area)

#36

