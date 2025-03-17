#1

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

#2

it_companies.add('Twitter')
print(it_companies)

#3

it_companies.update(['Spotify', 'Tesla'])
print(it_companies)

#4

it_companies.remove('Amazon')
print(it_companies)

#5

#La diferencia entre el remove y el discard es que el remove quita algo especifico y si no lo 
#encuentra lanza un error y el discard solo lo quita si tiene el dato
