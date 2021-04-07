class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class Stack:
	def __init__(self):
		self.head = None

	def __iter__(self):
		node = self.head
		while node:
			yield node
			node = node.next

	def __str__(self):
		templist = ["-> " + str(x.value) for x in self]
		return "\n".join(templist)

	def isEmpty(self):
		return False if self.head else True

	def push(self, value):
		node = Node(value)
		node.next = self.head
		self.head = node

	def pop(self):
		if not self.isEmpty():
			node = self.head
			self.head = node.next
			return node.value	
		else:
			return "Stack is empty"

	def peek(self):
		if not self.isEmpty():
			return self.head.value	
		else:
			return "Stack is empty"

	def delete(self):
		self.head = None

class Queue: # Queue to be implemented with two stacks
	def __init__(self):
		self.in_stack = Stack()
		self.out_stack = Stack()

	def __str__(self):
		while not self.in_stack.isEmpty():
			self.out_stack.push(self.in_stack.pop())

		returning_string = str(self.out_stack)

		while not self.out_stack.isEmpty():
			self.in_stack.push(self.out_stack.pop())

		return returning_string

	def isEmpty(self):
		return self.in_stack.isEmpty()

	def enqueue(self, value):
		self.in_stack.push(value)

	def dequeue(self):
		while not self.in_stack.isEmpty():
			self.out_stack.push(self.in_stack.pop())

		value = None
		if not self.out_stack.isEmpty():
			value = self.out_stack.pop()

			while not self.out_stack.isEmpty():
				self.in_stack.push(self.out_stack.pop())

		return value

	def peek(self):
		while not self.in_stack.isEmpty():
			self.out_stack.push(self.in_stack.pop())

		value = None
		if not self.out_stack.isEmpty():
			value = self.out_stack.peek()

			while not self.out_stack.isEmpty():
				self.in_stack.push(self.out_stack.pop())

		return value

	def delete(self):
		self.in_stack.delete()