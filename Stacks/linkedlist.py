# Creating singly linked list

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class SinglyLinkedList:
	def __init__(self): # O(1) time and space
		self.head = None
		self.tail = None
		self.size = 0


	def __iter__(self): # O(n) time and O(1) space
		node = self.head
		while node:
			yield node
			node = node.next

	def __len__(self): # O(1) time and space
		return self.size

	def append(self, value): # O(1) time and space
		node = Node(value)
		if not self.head:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

		self.size += 1
		return self.size - 1

	def insert(self, value, index):
		node = Node(value)
		if index >= self.size: # O(1) time and space
			return self.append(value)
		elif index == 0: # O(1) time and space
			node.next = self.head
			self.head = node
			self.size += 1
			return 0
		elif index > 0: # O(n) time and O(1) space
			currentNode = self.head
			count = 0
			while count < index - 1:
				currentNode = currentNode.next
				count += 1

			node.next = currentNode.next
			currentNode.next = node
			self.size += 1
			return index
		else:
			return "Index out of bound"
					
	def get(self, index):
		if index < 0 or index >= self.size:
			return "Index out of bound"
		else: # O(n) time and O(1) space
			node = self.head
			count = 0
			while count < index:
				node = node.next
				count += 1

			return node

	def remove(self, index):
		if index < 0 or index >= self.size:
			return "Index out of bound"
		elif index == 0: # O(1) time and space
			nodetoremove = self.head
			if nodetoremove.next:
				self.head = nodetoremove.next
				nodetoremove.next = None
			else:
				self.head = None
				self.tail = None
			self.size -= 1
			return nodetoremove.value
		else: # O(n) time and O(1) space
			node = self.head 
			count = 0
			while count < index - 1:
				node = node.next
				count += 1

			nodetoremove = node.next
			node.next = nodetoremove.next
			if self.tail is nodetoremove:
				self.tail = node

			nodetoremove.next = None
			self.size -= 1
			return nodetoremove.value

	def clear(self): # O(1) time and space
		self.head = None
		self.tail = None
		self.size = 0