class Item:
	def __init__(self, name, purchase_price):
		self.name = name
		self.purchase_price = purchase_price
		
		self.count_on_hand = 0
	
	def buy(self, n):
		self.count_on_hand += n
		return self.purchase_price * n
	
	def consume(self, n):
		self.count_on_hand -= n
	
	def __str__(self):
		return str(self.count_on_hand) + "x " + self.name

class Product:
	def __init__(self, name, sale_price, components):
		self.name = name
		self.sale_price = sale_price
		self.components = components
		
		self.count_on_hand = 0
	
	def make(self, n):
		self.count_on_hand += n
	
	def sell(self, n):
		self.count_on_hand -= n
		return self.sale_price * n
	
	def __str__(self):
		return str(self.count_on_hand) + "x " + self.name

class Inventory:
	def __init__(self):
		self.items = []
		self.products = []
		
		self.money = 0
	
	# Adds item and returns its handle
	def add_item(self, item):
		self.items.append(item)
		return len(self.items) - 1
	
	# Adds product and returns its handle
	def add_product(self, product):
		self.products.append(product)
		return len(self.products) - 1
	
	def buy_item(self, item_handle, n):
		item_to_buy = self.items[item_handle]
		self.money -= item_to_buy.buy(n)
	
	def make_product(self, product_handle, n):
		product_to_make = self.products[product_handle]
		
		for item_handle in product_to_make.components:
			if (self.items[item_handle].count_on_hand < n):
				raise ValueError("Can't make product '" + product_to_make.name + "'. Insufficient items.")
			
		for item_handle in product_to_make.components:
			self.items[item_handle].consume(n)
		
		product_to_make.make(n)
	
	def sell_product(self, product_handle, n):
		self.money += self.products[product_handle].sell(n)
	
	def __str__(self):
		ret = ""
		
		ret += "Items:\n"
		for item in self.items:
			ret += "- " + str(item) + "\n"
		
		ret += "\n"
		
		ret += "Products:\n"
		for product in self.products:
			ret += "- " + str(product) + "\n"
		
		ret += "\n"
		ret += "$" + str(self.money) + " in the bank."
		
		return ret

inv = Inventory()

stick_h = inv.add_item( Item("Stick", 5) )
spring_h = inv.add_item( Item("Spring", 7) )

controller_h = inv.add_product( Product("Controller", 30, [stick_h, spring_h]) )

print("Step 1:")
print(inv)

inv.buy_item(stick_h, -1)
inv.buy_item(spring_h, -1)

print("Step 2:")
print(inv)

inv.make_product(controller_h, -1)

print("Step 3:")
print(inv)

inv.sell_product(controller_h, -1)

print("Step 4: Profit!")
print(inv)