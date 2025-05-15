class dLinkedListNode:
	def __init__(self, data):
		self.data = data
		
		self.prev = None
		self.next = None
	
	def set_next(self, next_node):
		ret = None
		
		if next_node.prev is not None:
			next_node.prev.next = None
		
		if self.next is not None:
			ret = self.next
			self.next.prev = None
			
		next_node.prev = self
		self.next = next_node
		
		return ret
	
	def set_prev(self, prev_node):
		prev_node.set_next(self)
	
	def print(self):
		current_node = self
		print(current_node.data, end="")
		while current_node.next is not None:
			current_node = current_node.next
			print(", " + str(current_node.data), end="")
		
		print("")
	
	def get(self, index):
		if index == 0:
			return self
		else:
			return self.next.get(index-1)

list_a = dLinkedListNode(1)
list_a.set_next(dLinkedListNode(2))
list_a.next.set_next(dLinkedListNode(3))
list_a.next.next.set_next(dLinkedListNode(4))

list_b = dLinkedListNode("a")
list_b.set_next(dLinkedListNode("b"))
list_b.next.set_next(dLinkedListNode("c"))

list_a.print()
list_b.print()

node_with_2 = list_a.next
node_with_b = list_b.next
list_c = node_with_2.set_next(node_with_b)

list_c.next.set_next(list_a)
list_b.set_next(list_c)

#list_a.get(3).set_next(list_b)

print("------")

list_w = dLinkedListNode("W")
list_w.set_next(list_w)
list_w.print()