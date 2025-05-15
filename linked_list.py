class LinkedListNode:
	def __init__(self, data):
		self.data = data[0]
		self.next = None
		
		if len(data) > 1:
			self.next = LinkedListNode(data[1:])
	
	def set_next(self, next_node):
		self.next = next_node
	
	def get(self, index):
		if index == 0:
			return self.data
		else:
			return self.next.get(index-1)
	
	def getNode(self, index):
		if index == 0:
			return self
		else:
			return self.next.getNode(index-1)

	def getIterative(self, index):
		current_node = self
		while index > 0:
			current_node = current_node.next
			index = index - 1
		
		return current_node.data
	
	def prepend(self, data):
		new_node = LinkedListNode([self.data])
		new_node.next = self.next
		self.next = new_node
		self.data = data
	
	def newPrepend(self, data):
		new_node = LinkedListNode([data])
		new_node.next = self
		return new_node
	
	def append(self, data):
		current_node = self
		while current_node.next is not None:
			current_node = current_node.next
		
		current_node.next = LinkedListNode([data])
	
	def concat(self, data):
		current_node = self
		while current_node.next is not None:
			current_node = current_node.next
		
		current_node.next = LinkedListNode(data)
	
	def length(self):
		current_node = self
		num_hops = 0
		while current_node.next is not None:
			current_node = current_node.next
			num_hops += 1
		
		return num_hops + 1
	
	def print(self):
		current_node = self
		print(current_node.data, end="")
		while current_node.next is not None:
			current_node = current_node.next
			print(", " + str(current_node.data), end="")
		
		print("")

# (5) -> (*1) -> (2) -> (3) -> (4) - newPrepend
# (*5) -> (1) -> (2) -> (3) -> (4) - prepend

a = [1, 2, 3, 4]
b = a
b[0] = 9

print(a)

my_list = LinkedListNode([1, 2, 3, 4])
my_list.concat(["a", "b", "c"])
print(my_list.length())

my_list.print()