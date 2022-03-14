# This is an implementation of queue in python with list (Dynamic array property). This would not be an optimal queue, 
# but it is easy to implement

''' ------------------------------ FIRST IN FIRST OUT (FIFO) -------------------------------'''

class Queue:
	def __init__(self): # O(1) time and space
		self.list = []

	def __str__(self): # O(n) time and space
		templist = [str(x) for x in self.list]
		return " | ".join(templist)

	def isEmpty(self): # O(1) time and space
		if len(self.list) > 0:
			return False
		else:
			return True

	def enqueue(self, value): # Amotized O(1) time and O(1) space
		self.list.append(value)

	def peek(self): # O(1) time and space
		if not self.isEmpty():
			return self.list[0]
		else:
			return "List is empty"

	def dequeue(self): # O(n) time and O(1) space
		if not self.isEmpty():
			return self.list.pop(0)
		else:
			return "List is empty"

	def delete(self): # O(1) time and space
		self.list = []