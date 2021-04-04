# Creating a stack from list. I am going to set a max_size to the stack created this way, 
# the will stop the amotized nature of list (Dynamic array) when adding elements to it.

''' ---------------------- LAST IN FIRST OUT (LIFO) -----------------------------'''

class Stack: 
	def __init__(self, capacity): # O(n) time and space
		self.list = [None for _ in range(capacity)] # The prevents the amotized nature of list
		self.capacity = capacity
		self.size = 0

	def __str__(self):
		templist = []
		index = self.size
		while index > 0:
			index -= 1
			templist.append("-> " + str(self.list[index]))
		return "\n".join(templist)

	def isEmpty(self): # O(1) time and space
		if self.size > 0:
			return False
		else:
			return True

	def isFull(self): # O(1) time and space
		if self.size < self.capacity:
			return False
		else:
			return True

	def push(self, value): # O(1) time and space. Because capacity is defined, this is always O(1).
		if self.isFull():
			return "List is full"
		else:
			self.list[self.size] = value
			self.size += 1

	def peek(self): # O(1) time and space
		if self.isEmpty():
			return "List is empty"
		else:
			return self.list[self.size - 1]

	def pop(self): # O(1) time and space
		if self.isEmpty():
			return "List is empty"
		else:
			value = self.list[self.size - 1]
			self.list[self.size - 1] = None
			self.size -= 1
			return value
			
	def delete(self): # O(n) time and space
		self.list = [None for _ in range(self.capacity)]
		self.size = 0


