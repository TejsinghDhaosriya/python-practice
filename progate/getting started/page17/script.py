apple_price = 2
# Assign 10 to the money variable
money = 10

input_count = input('How many apples do you want?: ')
count = int(input_count)
total_price = apple_price * count

print('You will buy ' + str(count) + ' apples')
print('The total price is ' + str(total_price) + ' dollars')

# Add control flow based on the comparison of money and total_price
if money > total_price:
    print('You have bought'+str(count)+'apples')
    print('You have '+str(money-total_price)+' dollars left')
 
elif money ==total_price:
    print('You have bought'+str(count)+'apples')
    print('You have 0 dollars left')
else:
    print('You have bought 0 apples')
    print('You have 0 dollars left')