# This is a much better way of creating stacks that avoids the amotized nature of dynamic arrays, although not easy.

''' ---------------------- LAST IN FIRST OUT (LIFO) -----------------------------'''
import linkedlist

class Stack:
	def __init__(self):
		self.list = linkedlist.SinglyLinkedList()

	def __str__(self):
		templist = ["-> " + str(x.value) for x in self.list]
		return "\n".join(templist)

	def isEmpty(self): # O(1) time and space
		if self.list.head: # Can also be done like this: "len(self.list) > 0" with my better built list
			return False
		else: 
			return True

	def push(self, value): # O(1) time and space
		self.list.insert(value, 0)

	def peek(self): # O(1) time and space
		if self.isEmpty(): 
			return "List is empty"
		else:
			return self.list.head.value

	def pop(self): # O(1) time and space
		if self.isEmpty():
			return "List is empty"
		else:
			return self.list.remove(0)

	def delete(self): # O(1) time and space
		self.list.clear()
