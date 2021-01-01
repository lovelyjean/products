products = []

while True:
	name = input('product name: ')
	if name == 'q': #quit
		break
	price = input('product price: ')
	price = int(price)

	# p = []
	# p.append(name)
	# p.append(price)
	# p = [name, price]
	products.append([name, price])

print(products)

print(products[1][1])
