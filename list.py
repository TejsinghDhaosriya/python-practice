names1 = ['Amir', 'Barry', 'Chales', 'Dao']
names2 = names1   #referencing 
names3 = names1[:] #here data is copying into a new list

names2[0] = 'Alice'
print(names1)
print(names2)
print(names3)
names3[1] = 'Bob'

sum = 0
for ls in (names1, names2, names3):
    print(ls[0])
    if ls[0] == 'Alice':
        sum += 1
     #   print(ls[0])
    if ls[1] == 'Bob':
        sum += 10
   # print(ls)
print(sum)