''' In this file, I will be creating a custom doubly linked list '''

class Node: # Creating the node object for doubly linked list. In this intance, it has linke to the previous and next node.
	def __init__(self, value):
		self.value = value
		self.previous = None
		self.next = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self._size_ = 0

	def __iter__(self):
		node = self.head
		while node:
			yield node.value
			node = node.next

	def size(self):
		return self._size_ 

	def aslist(self): # Converst the doublylinkedlist to ordinary list
		list = []
		node = self.head
		while node:
			list.append(node.value)
			node = node.next

		return list # O(n) time and space complexity

	def reverse(self):
		list = []
		node = self.tail
		while node:
			list.append(node.value)
			node = node.previous

		return list

	def append(self, value):
		node = Node(value)
		if self._size_ == 0:
			self.head = node
			self.tail = node
		else:
			node.previous = self.tail
			node.next = self.tail.next
			self.tail.next = node
			self.tail = node

		self._size_ += 1
		return self._size_ - 1 # O(1) time and space complexity

	def insert(self, value, index):
		if index >= self._size_: # Runing this first makes sure that it catches the case when index is 0 and size is 0. 
								 # Hence tail and head are assigned
			return self.append(value)
		elif index == 0:
			nodetoadd = Node(value)
			nodetoadd.next = self.head
			self.head.previous = nodetoadd
			self.head = nodetoadd
			self._size_ += 1
			return 0 # O(1) time and space complexity
		else:
			nodetoadd = Node(value)
			node = self.head

			count = 0
			while count < index - 1:
				node = node.next
				count += 1

			nodetoadd.previous = node
			nodetoadd.next = node.next
			node.next = nodetoadd
			self._size_ += 1
			return count # O(n) time complexity and O(1) space complexity

	def get(self, index): # Getting value at specified index
		node = self.head

		count = 0
		while node:
			if count == index:
				return node.value 

			count += 1
			node = node.next

		return None # O(n) time complexity O(1) space complexity

	def indexof(self, value): # Getting the index of the first occurance of a value
		node = self.head

		index = 0
		while node:
			if node.value == value:
				return index

			index += 1
			node = node.next

		return None # O(n) time complexity O(1) space complexity

	def replace(self, value, index):
		newNode = Node(value)

		if index >= self._size_:
			return False
		elif index == 0:
			formerNode = self.head
			nodeAFN = formerNode.next
			newNode.next = nodeAFN
			if nodeAFN:
				nodeAFN.previous = newNode
			self.head = newNode
			if self.tail == formerNode:
				self.tail = newNode

			del(formerNode)
			return True  # O(1) time and space complexity
		elif index > 0:
			formerNode = self.head
			count = 0
			while count < index:
				nodeB4FN = formerNode
				formerNode = formerNode.next
				count += 1

			newNode.previous = nodeB4FN
			newNode.next = formerNode.next
			if formerNode.next:
				formerNode.next.previous = newNode
			nodeB4FN.next = newNode
			if self.tail == formerNode:
				self.tail = newNode

			del(formerNode)
			return True # O(n) time and O(1) space complexity
		else:
			return False

	def remove(self, index): # Removes item at specified index and returns the value removed
		if index >= self._size_:
			return None
		elif index == 0:
			nodeToDel = self.head
			self.head = nodeToDel.next
			self.head.previous = None
			if self.tail == nodeToDel:
				self.tail = nodeToDel.next

			value = nodeToDel.value
			self._size_ -= 1
			del(nodeToDel)
			return value  # O(1) time and space complexity
		elif index > 0:
			nodeTD = self.head
			count = 0
			while count < index:
				nodeB4NTD = nodeTD
				nodeTD = nodeTD.next
				count += 1

			nodeB4NTD.next = nodeTD.next
			if nodeTD.next:
				nodeTD.next.previous = nodeB4NTD
			if self.tail == nodeTD:
				self.tail = nodeB4NTD

			value = nodeTD.value
			self._size_ -= 1
			del(nodeTD)
			return value # O(n) time and O(1) space complexity
		else:
			return None

	def pop(self): # Removes item at the end of the list
		nodeTD = self.tail
		if nodeTD:
			self.tail = nodeTD.previous
			if self.tail:
				self.tail.next = None
			if self.head == nodeTD:
				self.head = nodeTD.previous

			self._size_ -= 1
			return self._size_ # O(1) time and O(1) space complexity

		return None

	def removeValue(self, value): # Removes first occurence of value
		nodeTD = self.head
		index = 0

		if nodeTD.value == value:
			self.head = nodeTD.next
			if nodeTD.next:
				nodeTD.next.previous = None
			if self.tail == nodeTD:
				self.tail = nodeTD.next

			self._size_ -= 1
			del(nodeTD)
			return index

		while nodeTD:
			nodeB4NTD = nodeTD
			nodeTD = nodeTD.next
			index += 1
			if nodeTD.value == value:
				nodeB4NTD.next = nodeTD.next
				if nodeTD.next:
					nodeTD.next.previous = nodeB4NTD
				if self.tail == nodeTD:
					self.tail = nodeB4NTD

				self._size_ -= 1
				del(nodeTD)
				return index

		return None # O(n) time and O(1) space complexity

	def clear(self): # Clears the list
		node = self.head
		while node:
			node.previous = None
			node = node.next

		self.head = None
		self.tail = None
		self._size_ = 0
		return True
		# Gabage collector will handle destroying the nodes and releasing memory locations used by nodes