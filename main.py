from string import Template


def main():
	cart = []
	cart.append(dict(item='Coke', price=8, qty=2))
	
	t = Template('$qty x $item = $price')
	
	print t.substitute(cart[0])
	
if __name__ == '__main__':
	main()