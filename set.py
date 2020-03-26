confusion = {}
confusion[1] = 1
print(confusion)
confusion['1'] = 2
print(confusion)
confusion[1] += 1
print(confusion)
sum = 0
for k in confusion:
    print("item are ",k)
    sum += confusion[k]
    print(sum)
print (sum)