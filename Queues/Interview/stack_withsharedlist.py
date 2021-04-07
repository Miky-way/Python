class Stack:
	def __init__(self, shared_list, start, end): # O(1) time and space
		self.list = shared_list
		self.start = start
		self.end = end
		self.size = 0

	def __len__(self): # O(1) time and space
		return self.size

	def __str__(self): # O(n) time and space
		templist = []
		index = self.start + self.size
		while index > self.start:
			index -= 1
			templist.append("-> " + str(self.list[index]))
		return "\n".join(templist)

	def capacity(self): # O(1) time and space
		return self.end - self.start + 1

	def isEmpty(self): # O(1) time and space
		if self.size > 0:
			return False
		else:
			return True

	def isFull(self): # O(1) time and space
		if self.size < self.capacity():
			return False
		else:
			return True

	def push(self, value): # O(1) time and space. Because capacity is defined, this is always O(1).
		if self.isFull():
			return "List is full"
		else:
			index = self.start + self.size
			self.list[index] = value
			self.size += 1

	def peek(self): # O(1) time and space
		if self.isEmpty():
			return "List is empty"
		else:
			index = self.start + self.size - 1
			return self.list[index]

	def pop(self): # O(1) time and space
		if self.isEmpty():
			return "List is empty"
		else:
			index = self.start + self.size - 1
			value = self.list[index]
			self.list[index] = None
			self.size -= 1
			return value
			
	def delete(self): # O(n) time and space
		for i in range(start, end+1):
			self.list[i] = None
		self.size = 0