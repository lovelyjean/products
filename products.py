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

for product in products:
	print(product[0], '的價格是', product[1])

with open('products.csv', 'w', encoding='utf-8') as f:
# with open('products.csv', 'w') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')