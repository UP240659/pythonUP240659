#1

listavacia = []

#2

lista = [10, 20, 30, 40, 50]

#3

print(len(lista))

#4

primerdato = lista[0]
datomedio = lista[3]
ultimodato = lista[-1]

print (primerdato, datomedio, ultimodato)

#5

datosmixtos = ['Daniel', 18, 1.85, 'Soltero', 'Aguascalientes' ]

#6

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple',  'IBM' , 'Oracle', 'Amazon']

#7

print(it_companies)

#8

print(len(it_companies))

#9

print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])

#10

it_companies[5] = 'Tesla'
print(it_companies)

#11

it_companies.append('Spotify')
print(it_companies)

#12

it_companies.insert(len(it_companies) // 2, "Adobe")
print(it_companies)

#13

it_companies[1] = it_companies[1].upper()  # Convertimos Google a mayúsculas
print(it_companies)

#14

joined_companies = " #; ".join(it_companies)
print(joined_companies)

#15

print("Microsoft" in it_companies)

#16

it_companies.sort()
print(it_companies)

#17

it_companies.reverse()
print(it_companies)

#18

print(it_companies[:3])


#19

print(it_companies[-3:])

#20

mitad =  len(it_companies) // 2
print(it_companies[mitad])

#22

del it_companies[0]
print(it_companies)

#23

it_companies.pop()
print(it_companies)

#24

it_companies.clear()
print(it_companies)

#25

del it_companies

#26

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)

#27

full_stack.insert(full_stack.index("Redux") + 1, "Python")
full_stack.insert(full_stack.index("Python") + 1, "SQL")

print(full_stack)

#Exercises: Level 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
min_age = ages[0]
max_age = ages[-1] 

print("Sorted ages: {ages}")
print("Min age: {min_age}, Max age: {max_age}")

ages.append(min_age)
ages.append(max_age)
print("Updated ages: {ages}")

ages.sort()  
n = len(ages)

if n % 2 == 0:  
    median_age = (ages[n//2 - 1] + ages[n//2]) / 2
else:  
    median_age = ages[n//2]

print("Median age: {median_age}")

average_age = sum(ages) / len(ages)
print("Average age: {average_age}")


age_range = max_age - min_age
print("Age range: {age_range}")

min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)

print("Min - Average: {min_diff}")
print("Max - Average: {max_diff}")


countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
n = len(countries)

if n % 2 == 0:  # Si la cantidad es par
    middle_countries = [countries[n//2 - 1], countries[n//2]]
else:  # Si es impar
    middle_countries = [countries[n//2]]

print(f"Middle country(ies): {middle_countries}")


first_half = countries[:(n + 1) // 2]  # Incluye un país más si es impar
second_half = countries[(n + 1) // 2:]

print(f"First half: {first_half}")
print(f"Second half: {second_half}")


first, second, third, *scandic_countries = countries

print(f"First 3 countries: {first}, {second}, {third}")
print(f"Scandic countries: {scandic_countries}")


