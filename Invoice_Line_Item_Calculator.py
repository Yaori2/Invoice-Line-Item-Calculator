i = 1 
while i > 0:
    def EnterPrice():
        price = float(input('Enter Price:  '))
        if price <= 0:
            raise ValueError('Invalid price entered')
        else:
            return price
    def EnterQuantity():
        quantity = int(input('Enter Quantity:  '))
        if quantity <= 0:
            raise ValueError('Invalid quantity entered.')
        else:
            return quantity
    print('Line Item Calculator')
    price = EnterPrice()
    quantity = EnterQuantity()
    value = price * quantity
    print('Price')
    print(price)
    print('Quantity')
    print(quantity)
    print('Total')
    print(value)
    answer = input('Enter another item? y/n   ')
    if answer == "n":
        break
    else:
        print('Restarting')
    
