

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

A.update(B)
print(A)
C = A|B

#Exercise 2 (Level 2)
print(A.intersection(B))

#3
print(A.issubset(B))

#4 

print(A.isdisjoint(B))

#5 

D = B|A

print(C==D)

#6
print(A.symmetric_difference(B))

#7

del A
del B
print(B.issuperset(A))

