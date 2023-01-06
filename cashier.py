item_name= input('Input menu: ')
price= int(input('Input Price of menu: '))
Quantity = int(input('input your Quantity:'))
Quantity2 = price * Quantity
total_Money = int(input('Input your money: '))
return_money = total_Money - Quantity2

teks = f'''
Your Nota

Name item: {item_name}
Price: {price}
Quantity: {Quantity}
Total Price: {Quantity2}
Total Money: {total_Money}
Return: {return_money}

thank you for buying
'''

file = open('Nota.txt', 'w')

file.write(teks)

