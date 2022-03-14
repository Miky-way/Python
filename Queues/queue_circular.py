# This is an implementation of queue in python with list of fixed capacity. This is a faster queue unlike the implementation
# without capacity

''' ------------------------------ FIRST IN FIRST OUT (FIFO) -------------------------------'''

class Queue:
	def __init__(self, capacity):  # O(1) time and O(n) space
		self.list = capacity * [None] 
		self.capacity = capacity
		self.top = -1	 # -------- Dequeue and peek at the top
		self.bottom = -1 # -------- Enqueue at the bottom

	def __iter__(self): # O(n) time and O(1) space
		while self.top != self.bottom:
			yield self.list[self.top]
			self.top += 1
			if self.top == self.capacity:
				self.top = 0
		else:
			if self.top is not -1:
				yield self.list[self.top]

	def __str__(self): # O(n) time and space
		templist = []
		index = self.top
		while index is not self.bottom:
			templist.append(str(self.list[index]))
			index = self.next(index)
		else:
			if index is not -1:
				templist.append(str(self.list[index]))
		return " | ".join(templist)

	def next(self, index): # O(1) time and space
		index += 1
		if index == self.capacity:
			index = 0
		return index

	def prev(self, index): # O(1) time and space
		index -= 1
		if index == -1:
			index = self.capacity
		return index

	def isEmpty(self): # O(1) time and space
		if self.top is self.bottom and self.top is -1:
			return True
		else:
			return False

	def isFull(self): # O(1) time and space
		if self.next(self.bottom) == self.top:
			True
		else:
			False

	def enqueue(self, value): # O(1) time and space
		if not self.isFull():
			init_bottom_index = self.bottom

			self.bottom = self.next(self.bottom)
			self.list[self.bottom] = value

			if init_bottom_index is -1:
				self.top = self.next(self.top)
		else:
			return "List is full"

	def dequeue(self): # O(1) time and space
		if not self.isEmpty():
			value = self.list[self.top]
			self.list[self.top] = None
			self.top = self.next(self.top)

			if self.top is self.bottom:
				self.top = -1
				self.bottom = -1

			return value
		else:
			return "List is empty"

	def peek(self): # O(1) time and space
		if not self.isEmpty():
			return self.list[self.top]
		else:
			return "List is empty"

	def delete(self): # O(1) time and space
		self.list = self.capacity * [None] 
		self.top = -1
		self.bottom = -1 