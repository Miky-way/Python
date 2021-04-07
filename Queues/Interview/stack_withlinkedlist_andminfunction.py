# This is a much better way of creating stacks that avoids the amotized nature of dynamic arrays, although not easy.

class Node:
	def __init__(self, value):
		self.value = value
		self.min = None
		self.next = None

	def setMin(self, min_element):
		self.min = min_element

''' ----------------------------STACK WITH LINKED LIST ---------------------------------'''
''' -------------------------- LAST IN FIRST OUT (LIFO) --------------------------------'''
'''------------------------------ HAS MIN FUNCTION -------------------------------------'''

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

	def isEmpty(self): # O(1) time and space
		if self.head:
			return False
		else: 
			return True

	def push(self, value): # O(1) time and space
		node = Node(value)
		if self.head:
			node.setMin(value) if value < self.head.min else node.setMin(self.head.min)
			node.next = self.head
			self.head = node
		else:
			node.setMin(value)
			self.head = node

	def peek(self): # O(1) time and space
		if self.isEmpty(): 
			return "List is empty"
		else:
			return self.head.value

	def pop(self): # O(1) time and space
		if self.isEmpty():
			return "List is empty"
		else:
			currenthead = self.head
			self.head = currenthead.next
			currenthead.next = None
			return currenthead.value

	def min(self): # O(1) time and space
		return self.head.min

	def delete(self): # O(1) time and space
		self.head = None
