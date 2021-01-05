import os

# read file
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

# user input
def user_input(products):
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
	return products

def print_product(products):
	for product in products:
		print(product[0], '的價格是', product[1])

# write file
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('yeah! file found!')
		products = read_file(filename)
	else:
		print('file not found...')

	products = user_input(products)
	print_product(products)
	write_file('products.csv', products)

main()