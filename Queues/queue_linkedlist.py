# This is an implementation of queue in python with linkedlist. It's the optimal solution, although not as easy to create.
# But once you have the linkedlist handy as I do, then eveything else if just easy going from there on.

''' ------------------------------ FIRST IN FIRST OUT (FIFO) -------------------------------'''
import linkedlist

class Queue:
	def __init__(self): # O(1) time and space
		self.list = linkedlist.SinglyLinkedList()

	def __str__(self): # O(n) time and space
		templist = [str(i.value) for i in self.list]
		return " | ".join(templist)

	def isEmpty(self): # O(1) time and space
		if len(self.list) > 0:
			return False
		else:
			return True

	def enqueue(self, value): # O(1) time and space
		self.list.append(value)

	def peek(self):
		if not self.isEmpty(): # O(1) time and space
			return self.list.head.value
		else:
			return "List is empty"

	def dequeue(self):
		if not self.isEmpty(): # O(1) time and space
			return self.list.remove(0)
		else:
			return "List is empty"

	def delete(self): # O(1) time and space
		self.list.clear()