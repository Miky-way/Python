''' In this file, I would be creating a custom singly linked list module '''

class Node: # This would be the node structure for the list
	def __init__(self, value):
		self.value = value
		self.next = None

class SinglyLinkedList: # The main list class

	def __init__(self):
		self.head = None
		self.tail = None
		self._size_ = 0 

	def __iter__(self): # An iterable function that allows iteration of the list items
		node = self.head
		while node:
			yield node
			node = node.next

	def __len__(self):
		return self._size_

	def size(self): # Returns the current size of the linked list
		return self._size_

	def aslist(self): # Converst the singlylinkedlist to ordinary list
		list = []
		node = self.head
		while node:
			list.append(node.value)
			node = node.next

		return list # O(n) time and space complexity

	def fromlist(self, list):
		for i in list:
			self.append(i)

	def append(self, value): # Method appends node to the end of the linked list
		node = Node(value)
		if self._size_ == 0:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

		self._size_ += 1
		return self._size_ - 1 # O(1) time and space complexity

	def insert(self, value, index): # Method inserts node in provided index position
		if index >= self._size_: # Runing this first makes sure that it catches the case when index is 0 and size is 0. 
								 # Hence tail and head are assigned
			return self.append(value)
		elif index == 0:
			nodetoadd = Node(value)
			nodetoadd.next = self.head
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
			newNode.next = formerNode.next
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

			newNode.next = formerNode.next
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
			if self.tail == nodeTD:
				self.tail = nodeB4NTD

			value = nodeTD.value
			self._size_ -= 1
			del(nodeTD)
			return value # O(n) time and O(1) space complexity
		else:
			return None

	def pop(self): # Removes item at the end of the list
		return self.remove(self._size_ - 1) # O(n) time and O(n) space complexity

	def removeValue(self, value): # Removes first occurence of value
		nodeTD = self.head
		index = 0

		if nodeTD.value == value:
			self.head = nodeTD.next
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
				if self.tail == nodeTD:
					self.tail = nodeB4NTD

				self._size_ -= 1
				del(nodeTD)
				return index

		return None # O(n) time and O(1) space 

	def reverse(self):
		headnode = self.head
		node = self.head
		if headnode: node = node.next

		while node: 
			self.insert(node.value, 0)
			currentnode = node
			node = node.next

			del(currentnode)

		if headnode: headnode.next = None
		self.tail = headnode
 		# O(n) time and O(1) space

	def clear(self): # Clears the list
		self.head = None
		self.tail = None
		self._size_ = 0
		# Gabage collector will handle destroying the nodes and releasing memory locations used by nodes
