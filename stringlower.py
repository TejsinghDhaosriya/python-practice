names1 = ['Amir', 'Barry', 'Chales', 'Dao']
names2 = [name.lower() for name in names1]
print(names2)
print (names2[2][0])




vec = [2, 4, 6]
print()
print([3*x for x in vec if x > 3])


#vec = [2, 4, 6]

x1 = [x, x**2 for x in vec]

print (x1)