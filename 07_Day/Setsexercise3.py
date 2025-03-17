age = [22, 19, 24, 25, 26, 24, 25, 24]

#1

age_set = set(age)
print(type(age_set))

#2

if (len(age)>len(age_set)):
    print('La lista tiene más ')
elif(len(age)<len(age_set)):
    print('El set tiene mas ')
else:
    print('tienen la misma cantidad de elementos')

#3

sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.replace(".", "").split() 
unique_words= set(words)
print('Unique words:',unique_words)

