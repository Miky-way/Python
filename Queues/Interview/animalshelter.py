class Node:
	def __init__(self, number, animal_type):
		self.number = number
		self.type = animal_type
		self.next = None
		self.prev = None

	def __str__(self):
		return "Animal number: "+str(self.number)+"\tAnimal type: "+self.type

class AnimalQueue:
	def __init__(self):
		self.head = None
		self.tail = None
		self.animal_number = 0

	def __iter__(self): # O(n) time and O(1) space
		node = self.head
		while node:
			yield node
			node = node.next

	def __str__(self): # O(n) time and space
		templist = [str(i) for i in self]
		return "\n".join(templist) 

	def isEmpty(self):
		return False if self.head else True
		
	def enqueue(self, animal_type):
		self.animal_number += 1
		node = Node(self.animal_number, animal_type)
		if self.head:
			self.head.prev = node
		else:
			self.tail = node
		node.next = self.head
		self.head= node

	def dequeueAny(self):
		if not self.isEmpty():
			return self.removeNode(self.tail)
		else:
			return "Queue is empty"

	def dequeueDog(self):
		if not self.isEmpty():
			node = self.tail

			while node:
				if node.type is "Dog": return self.removeNode(node)
				node = node.prev
			
			return "No more dogs in queue"
		else:
			return "Queue is empty"

	def dequeueCat(self):
		if not self.isEmpty():
			node = self.tail
			
			while node:
				if node.type is "Cat": return self.removeNode(node)
				node = node.prev
			
			return "No more cats in queue"
		else:
			return "Queue is empty"

	def removeNode(self, node):
		nodebefore = node.prev
		nodenext = node.next
		if nodebefore:
			nodebefore.next = nodenext
		if nodenext:
			nodenext.prev = nodebefore

		if node is self.head:
			self.head = nodenext
		if node is self.tail:
			self.tail = nodebefore

		return str(node)

	def delete(self):
		node = self.head
		while node:
			node.prev = None
			node = node.next

		self.head = None
		self.tail = None
