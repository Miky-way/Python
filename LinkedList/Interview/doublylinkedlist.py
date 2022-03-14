class Node:
	def __init__(self, value):
		self.value = value
		self.prev = None
		self.next = None

	def __str__(self):
		return str(self.value)

class DoublyLinkedList:
	def __init__(self):
		self.size = 0
		self.head = None
		self.tail = None

	def __iter__(self):
		node = self.head
		while node:
			yield node
			node = node.next

	def __str__(self):
		listStr = [str(x.value) for x in self]
		return " -> ".join(listStr) 

	def __len__(self):
		return self.size

	def listfromend(self):
		list = []
		node = self.tail
		while node:
			list.append(node.value)
			node = node.prev

		return list

	def fromlist(self, list):
		for i in list:
			self.append(i)

	def append(self, value):
		nodetoadd = Node(value)
		if self.size == 0:
			self.head = nodetoadd
			self.tail = nodetoadd
		else:
			formertail = self.tail
			nodetoadd.prev = formertail
			formertail.next = nodetoadd
			self.tail = nodetoadd

		self.size += 1
		return self.size - 1

	def insert(self, value, index):
		if index >= self.size:
			return self.append(value)
		elif index == 0:
			nodetoadd = Node(value)
			formerhead = self.head
			formerhead.prev = nodetoadd
			nodetoadd.next = formerhead
			self.head = nodetoadd
			self.size += 1
			return 0
		elif index > 0:
			nodetoadd = Node(value)
			node = self.head

			count = 0
			while count < index:
				nodeBIN = node
				node = node.next
				count += 1

			nodetoadd.prev = nodeBIN
			nodetoadd.next = node
			nodeBIN.next = nodetoadd
			node.prev = nodetoadd
			self.size += 1
			return count
		else:
			return "Invalid index"

	def get(self, index):
		if index < 0 or index >= self.size:
			return "Invalid index"
		else:
			node = self.head
			count = 0
			while count < index:
				node = node.next
				count += 1

			return node

	def remove(self, index):
		if index < 0 or index >= self.size:
			return "Invalid index"
		elif index == 0:
			nodetodelete = self.head
			self.head = nodetodelete.next
			if self.head:
				self.head.prev = None
			elif self.tail == nodetodelete:
				self.tail = None

			nodetodelete.next = None
			self.size -= 1
			return nodetodelete.value
		else:
			node = self.head
			count = 0
			while count < index:
				node = node.next
				count += 1

			nodebefore = node.prev
			nodenext = node.next
			nodebefore.next = nodenext
			if nodenext:
				nodenext.prev = nodebefore

			if self.tail == node:
				self.tail = nodebefore

			node.prev = None
			node.next = None
			self.size -= 1
			return node.value

	def removeNode(self, node):
		if node:
			nodebefore = node.prev
			nodenext = node.next
			if nodebefore:
				nodebefore.next = nodenext
			if nodenext:
				nodenext.prev = nodebefore

			if node == self.head:
				self.head = nodenext
			if node == self.tail:
				self.tail = nodebefore

			del(node)
			return True

		return False

	def pop(self):
		if self.tail:
			nodetodelete = self.tail
			self.tail = nodetodelete.prev
			if self.tail:
				self.tail.next = None
			if self.head == nodetodelete:
				self.head = None

			nodetodelete.prev = None
			self.size -= 1
			return nodetodelete.value
		else:
			return None

	def clear(self):
		node = self.head
		while node:
			node.prev = None
			node = node.next

		self.head = None
		self.tail = None
		self.size = 0
		return True