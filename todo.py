from datetime import *

class ToDoItem:
	def __init__(self, text, time):
		self.text = text
		self.time = time
		self.completed = False
	
	def mark_complete(self):
		self.completed = True
	
	def is_overdue(self):
		return datetime.now() > self.time
	
	def get_time(self):
		return self.time
	
	def __str__(self):
		return self.text #+ " by " + self.time.strftime("%I:%M%p %B %d, %Y")
	
	def __repr__(self):
		return str(self)

class ToDoList:
	def __init__(self):
		self.items = []
	
	def add_item(self, item):
		self.items.append(item)
		self.items.sort(key = ToDoItem.get_time)
	
	def __str__(self):
		ret = ""
		for item in self.items:
			ret += "- " + str(item) + "\n"
		
		return ret
	
	def __repr__(self):
		ret = ""
		for item in self.items:
			ret += str(item) + "\n"
		
		return ret

my_list = ToDoList()

while True:
	inp = input().strip().split(" ", 1)
	command = inp[0]
	
	if command == "exit":
		break
		
	if command == "show":
		print(my_list)
	
	if len(inp) < 2:
		continue
	
	data = inp[1]
	
	if command == "new":
		my_list.add_item(ToDoItem(data, datetime.now()))
	
	if command == "save":
		fout = open(data, "w")
		fout.write(repr(my_list))
		fout.close()
	
	if command == "load":
		fin = open(data, "r")
		for datum in fin.read().split("\n"):
			my_list.add_item(ToDoItem(datum, datetime.now()))
		
		fin.close()