#1

empty_tuple = ()
print(empty_tuple)  

#2

sisters = ("Alice", "Maria")
brothers = ("John", "Mark")

#3

siblings = sisters + brothers
print(siblings)

#4

print(len(siblings))

#5

family_members = siblings + ("Father", "Mother")
print(family_members)

#Exercises: Level 2

siblings, father, mother = family_members[:4], family_members[4], family_members[5]
print(siblings)  
print(father)    
print(mother)   

#2

fruits = ('Apple', 'Banana', 'Cherry')
vegetables = ('Carrot', 'Broccoli', 'Spinach')
animal_products = ('Milk', 'Eggs', 'Cheese')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

middle_item = food_stuff_tp[len(food_stuff_tp) // 2]
print(middle_item)  

middle_item_list = food_stuff_lt[len(food_stuff_lt) // 2]
print(middle_item_list)  

primeros = food_stuff_lt[:3]
ultimos = food_stuff_lt[-3:]
print(primeros)  
print(ultimos)   

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)  # False

print('Iceland' in nordic_countries)  # True



