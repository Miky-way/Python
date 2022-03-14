class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None

class SetOfStacks:
	def __init__(self, substack_capacity): # O(1) and space 
		self.head = None
		self.tail = None
		self.size = 0
		self.substack_capacity = substack_capacity
		self.substack = []

	def __iter__(self):
		node = self.head
		while node:
			yield node
			node = node.next

	def __str__(self): # O(n) and space
		listoflist = []

		counter = 0
		sublist = []
		for i in self:
			sublist.append(i.value)
			counter += 1
			if counter == self.substack_capacity:
				listoflist.append(sublist)
				counter = 0
				sublist = []
		else:
			if len(sublist) > 0:
				listoflist.append(sublist)

		returning_str = ""
		for i in range(len(listoflist[0])):

			for sublist in listoflist:
				if len(sublist) > i: returning_str += str(sublist[i]) + "\t"
				else: returning_str += "  \t"

			returning_str += "\n"

		return returning_str

	def isEmpty(self): # O(1) time and space
		if self.head:
			return False
		else: 
			return True

	def push(self, value): # O(len(self.substack)) time and O(1) space
		node = Node(value)
		if self.head: 
			self.head.prev = node  
			# Adjust the substack elements
			for i in range(len(self.substack)): self.substack[i] = self.substack[i].prev

			self.size += 1
			if self.size % self.substack_capacity == 0: self.substack.append(self.tail)
		else:
			self.substack.append(node)
			self.tail = node
		node.next = self.head
		self.head = node

	def peek(self): # O(1) time and space
		if self.isEmpty(): 
			return "List is empty"
		else:
			return self.head.value

	def pop(self): # O(len(self.substack)) time and O(1) space
		if self.isEmpty():
			return "List is empty"
		else:
			currenthead = self.head
			self.head = currenthead.next
			if self.head: self.head.prev = None
			if self.tail is currenthead: self.tail = None
			
			# Adjust the substack elements
			for i in range(len(self.substack)): 
				self.substack[i] = self.substack[i].next
				if self.substack[i] == None: self.substack.pop()

			self.size -= 1
			currenthead.prev = None
			return currenthead.value

	def popAt(self, index): # O(len(self.substack)) time and O(1) space
		if len(self.substack) > index and index >= 0:
			if index == 0:
				return self.pop()
			else:
				nodetopop = self.substack[index]
				nodetopop.prev.next = nodetopop.next
				if nodetopop.next: nodetopop.next.prev = nodetopop.prev

				self.substack[index] = nodetopop.next
				if self.substack[index] == None: self.substack.pop()

				# Adjust the substack elements
				for i in range(index + 1, len(self.substack)): 
					self.substack[i] = self.substack[i].next
					if self.substack[i] == None: self.substack.pop()

				self.size -= 1
				nodetopop.prev = None
				nodetopop.next = None
				return nodetopop.value
		else:
			return "Index out of bound"

	def delete(self): # O(1) time and space
		self.head = None
		self.tail = None
		self.size = 0
		self.substack = []




# ----------------------There own implementation--------------------------

# This implementation has a problem. Pop_at(index) will just pop from the specified stack,
# it doesn't care to roll over from the next stack so that only the last stack  will be the only stack with empty cells.

''' 
	Popping substack[4]: 36

	59	  	14	  	87	85	1	50	68	
	1	  	67	  	  	21	3	92	  	
	24	  	94	  	  	17	45	29	  	
	0	  	68	  	  	12	11	64	  	
	25	  	9	  	  	74	78	63	  	
	20	  	48	  	  	90	26	81	  	
	75	  	  	  	  	  	41	75	  	

	You will notice the empty stacks in [1] [3] and the ones with just one element in [4] and [8] 
	A solution would be to always check for emptiness of stack when popAT is called, although this doens't solve 
	the case of stacks that are not the last not being full
	'''

class PlateStack():
	def __init__(self, capacity):
		self.capacity = capacity
		self.stacks = []

	def __str__(self):
		
		returning_str = ""
		for i in range(len(self.stacks[0])):
			for substack in self.stacks:
				if len(substack) > i: returning_str += str(substack[i]) + "\t"
				else: returning_str += "  \t"
			
			returning_str += "\n"

		return returning_str
    
	def push(self, item):
		if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity:
			self.stacks[-1].append(item)
		else:
			self.stacks.append([item])
    
	def pop(self):
		while len(self.stacks) and len(self.stacks[-1]) == 0: self.stacks.pop()

		if len(self.stacks) == 0:
			return None
		else:
			return self.stacks[-1].pop()
    
	def popAt(self, stackNumber):
		# if len(self.stacks[stackNumber]) > 0:
		# 	return self.stacks[stackNumber].pop()
		# else:
		# 	return None

		# Solution
		if len(self.stacks[stackNumber]) > 0:
			value = self.stacks[stackNumber].pop()

			if len(self.stacks[stackNumber]) <= 0:
				self.stacks.pop(stackNumber)

			return value
		else:
			return None