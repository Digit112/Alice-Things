class topping:
	def __init__(self, name):
		self.name = name
	
	def __eq__(self, other):
		return self.name == other.name

class pizza:
	def __init__(self, diam, num_slices, toppings):
		self.diam = diam
		self.num_slices = num_slices
		self.toppings = toppings
	
	def __eq__(self, other):
		diam_equal = self.diam == other.diam
		num_slices_equal = self.num_slices == other.num_slices
		toppings_equal = len(self.toppings) == len(other.toppings)
		
		return diam_equal and num_slices_equal and toppings_equal
	
	def __ne__(self, other):
		return not (self == other)
	
	def __lt__(self, other):
		if self.diam < other.diam:
			return True
		elif self.diam == other.diam:
			if len(self.toppings) < len(other.toppings):
				return True
			elif len(self.toppings) == len(other.toppings):
				if self.num_slices < other.num_slices:
					return True
		
		return False
	
	def __le__(self, other):
		return self < other or self == other
	
	def __gt__(self, other):
		return not self <= other

pizz_a = pizza(16, 4, [topping("mush")])
pizz_b = pizza(16, 4, [topping(pizz_a)])
pizz_c = pizza(16, 4, [topping(pizz_b)])

print(pizz_c.toppings[0].name.toppings[0].name.toppings[0].name)

print("a < b: " + str(pizz_a < pizz_b))
print("a = b: " + str(pizz_a == pizz_b))
print("a > b: " + str(pizz_a > pizz_b))
