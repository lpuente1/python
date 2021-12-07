price = int(input('Enter price of product: '))  #integer converted to string
quantity = int(input('Enter quantity: '))       #user enters quantity. integer converted to string
amount = price * quantity                       #total amount is result of price and quantity

if amount > 2000:                          #if amount is greater than or equal to 2000 dollars
    discount = amount*0.20                 #discount is 20 percent
else:                                      #if amount is less than 2000 dollars
    discount = 0                           #discount not applied

net_amount = amount - discount             #total is equal to the amount and discount

print('Bill amount:',amount)              #total bill amount
print('Discount:',discount)               #total with or without discount
print('Your bill amount is',net_amount)   #overall amount