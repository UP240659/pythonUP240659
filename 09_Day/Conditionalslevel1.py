#Exercise 1 
edad = int(input('Ingresa tu edad:'))

if (edad>=18):
    print('Eres lo suficientemente mayor para manejar')
else:
    print('Necesitas',(18-edad),'años para manejar ')
#Exercise 2 

age1 = int(input('Mi edad:'))
age2 = int(input('Tu edad:'))

dif = age1 - age2 
if (age2>age1 and dif>1):
    print('Tu eres',dif,'mas grande que yo ')
elif(age2>age1 and dif==1):
    print('Eres 1 año mayor que yo')
elif (age1>age2 and dif==1):
    print('Soy un año mayor que tu ')
else:
     print('Soy',dif,'años mayor que tu ')

#Exercise 3 
n1 = int(input('Enter number one:'))
n2  =int(input('Enter number two:'))

if (n1>n2):
    print(n1,'is greater than',n2)
else:
     print(n2,'is greater than',n1)