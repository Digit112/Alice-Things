class LinkedListNode:
	def __init__(self, data):
		self.data = data
		self.next = None
	
	def append(self, next_node):
		self.next = next_node

first_elem = LinkedListNode(1)
second_elem = LinkedListNode(2)
third_elem = LinkedListNode(3)

second_elem.append(third_elem)
first_elem.append(second_elem)

print(first_elem.next.next.data)