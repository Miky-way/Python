import singlylinkedlist as sll
from Interview import doublylinkedlist as dll
from random import randint

def gendll(n, min_val, max_val):
	doublylist = dll.DoublyLinkedList()
	for i in range(n):
		doublylist.append(randint(min_val, max_val))

	return doublylist


def gensll(n, min_val, max_val):
	singlylist = sll.SinglyLinkedList()
	for i in range(n):
		singlylist.append(randint(min_val, max_val))

	return singlylist

def intersect(list1, n, min_val, max_val):
	singlylist = sll.SinglyLinkedList()

	list1_len = len(list1)
	node = list1.head
	for i in range(n):
		singlylist.append(randint(min_val, max_val))
		if i > 4:
			node = node.next
			list1_len -= 1

	singlylist.tail.next = node
	singlylist.tail = list1.tail
	singlylist._size_ += list1_len

	return singlylist


# doublylist = gendll(15, 10, 50)
# singlylist = gensll(15, 10, 50)

# print(str(doublylist))
# print(len(doublylist))
# print(doublylist.reverse())
# print(singlylist.aslist())




#1 Write a function that remove duplicate from an unsorted list

def removeDupInit(linkedlist):
	# Would have taken the range() approach if lookup in linked list was O(1), but since it's O(n) using that
	# approach would result in an O(n**3) time complexity

	''' THE BELOW CODE LEADS TO CONCURRENT MODIFICATION '''
	# for i in range(len(linkedlist)):
	# 	for j in range(i+1):
	# 		val1 = linkedlist.get(i) # O(n)
	# 		val2 = linkedlist.get(j) # O(n)

	# 		if val1 == val2:
	# 			linkedlist.remove(j) # O(n) Results in concurrent modification


	''' ERROR WITH THE BELOW CODE IS THAT 'j' IS'T THE INDEX TO REMOVE BUT THE ACTUAL VALUE, AND LEADS CONCURRENT MODIFICATION '''
	# for i in linkedlist: # O(n)
	# 	for j in linkedlist: # O(n)
	# 		if i == j:
	# 			linkedlist.remove(j) # O(n) Results in concurrent modification 

	''' BETTER APPROACH '''
	newlinkedlist = dll.DoublyLinkedList() # O(n) space
	for i in linkedlist: # O(n) time
		isUnique = True
		for j in newlinkedlist: # O(n) time
			if i.value == j.value:
				isUnique = False
				break

		if isUnique:
			newlinkedlist.append(i.value)

	return newlinkedlist # 0(n**2) time and O(n) space

def removeDupBetter(linkedlist):
	setvalues = set() # O(n)  space
	newlinkedlist = dll.DoublyLinkedList() # 0(n) space

	for i in linkedlist: # O(n) time
		if i.value not in setvalues:
			setvalues.add(i.value)
			newlinkedlist.append(i.value)

	return newlinkedlist # O(n) time and O(n**2) space

def removeDupMuchBetter1(linkedlist):
	setvalues = set() # O(n) space
	for i in linkedlist: # O(n) time
		if i.value in setvalues:
			linkedlist.removeNode(i)
		else:
			setvalues.add(i.value)
	# O(n) time and space

def removeDupMuchBetter2(linkedlist):
	for i in linkedlist: # O(n) time
		node = i.next
		while node:
			if i.value == node.value:
				linkedlist.removeNode(node)
			node = node.next
	# O(n**2) time and O(1) space

# print("After Init", removeDupInit(doublylist))
# print("After better", removeDupBetter(doublylist))
# removeDupMuchBetter2(doublylist)
# print("After much better", doublylist)

# For an ordered linked list, it becomes easy and less space consuming
def removeDupOrdered(linkedlist):
	for i in linkedlist: # O(n) time
		if i.prev:
			if i.value == i.prev.value:
				linkedlist.removeNode(i)

	# O(n) time and O(1) space

doublyorderedlist = dll.DoublyLinkedList()
doublyorderedlist.append(0)
doublyorderedlist.append(1)
doublyorderedlist.append(1)
doublyorderedlist.append(2)
doublyorderedlist.append(4)
doublyorderedlist.append(5)
doublyorderedlist.append(5)
doublyorderedlist.append(6)
doublyorderedlist.append(7)
doublyorderedlist.append(8)
doublyorderedlist.append(8)
doublyorderedlist.append(9)
doublyorderedlist.append(10)
doublyorderedlist.append(10)
doublyorderedlist.append(11)
doublyorderedlist.append(11)
doublyorderedlist.append(11)
doublyorderedlist.append(11)
doublyorderedlist.append(12)
doublyorderedlist.append(13)
doublyorderedlist.append(14)
doublyorderedlist.append(15)
doublyorderedlist.append(15)
doublyorderedlist.append(15)
doublyorderedlist.append(15)

# print(str(doublyorderedlist))
# removeDupOrdered(doublyorderedlist)
# print(str(doublyorderedlist))



#2 Implement an algorithm to find the nth to last element in a singly linked list (Mis undertood question)

def find_nthToLast(singlylinkedlist, n): # If we still need the linkedlist and we are returning as list
	if n >= singlylinkedlist.size() or n < 0:
		return "Index out of bound"

	list = [] # O(n) space
	node = singlylinkedlist.head
	count = 0
	while node: # O(n) time 
		if count >= n:
			list.append(node.value)

		node = node.next
		count += 1

	return list # O(n) time and space 

def find_nthToLast1(singlylinkedlist, n): # O(n) time and O(1) space complexity
	if n >= singlylinkedlist.size() or n < 0:
		return "Index out of bound"

	node = singlylinkedlist.head
	count = 0

	if count == n:
		return

	while node: # O(n) time 
		count += 1

		if count == n:
			singlylinkedlist.head = node.next
			node.next = None
			return

		node = node.next

# print(singlylist.aslist())
# # print(find_nthToLast(singlylist, 0)) # method 1 test
# find_nthToLast1(singlylist, 5)
# print(singlylist.aslist())


#2 Implement an algorithm fo fint the nth element from the last of a singly linked list

def find_nthfromlastMyAmazingList(singlylist, n):
	if n > singlylist.size() or n <= 0:
		return "Index out of bound"

	index = singlylist.size() - n
	node = singlylist.head

	count = 0
	while node: # O(n) time 
		if count == index:
			return node.value

		node = node.next
		count += 1

	return None # O(n) time and O(1) space


def find_nthfromlast(singlylist, n):
	if n <= 0:
		return "Index out of bound"

	tempList = [] # O(n) space
	node = singlylist.head

	count = 0
	while node: # O(n) time 
		tempList.append(node.value)
		node = node.next
		count += 1

	index = count - n

	if index < 0:
		return "Index out of bound"

	return tempList[index] # O(n) time and O(n) space

def find_nthfromlastbetter(singlylist, n):
	if n <= 0:
		return "Index out of bound"

	pointerStart = None
	pointerEnd = singlylist.head

	count = 1 # It's starting from 1 because we are not looking for index here but for the nth element
	while pointerEnd: # O(n) time 
		pointerEnd = pointerEnd.next

		if count == n:
			pointerStart = singlylist.head
		elif count > n:
			pointerStart = pointerStart.next

		count += 1

	if pointerStart:
		return pointerStart.value
	else:
		return "Index out of bound" # O(n) time and O(1) space

# print(singlylist.aslist())
# print(find_nthfromlastMyAmazingList(singlylist, 5)) 
# print(find_nthfromlast(singlylist, 3))
# print(find_nthfromlastbetter(singlylist, 16))


#3 Write code to partition a linkedlist around a value x, such that all nodes less 
#  than x come before all nodes greater than or equal to x
def partition(linkedlist, x):
	lesslist = dll.DoublyLinkedList() # O(n) space
	greaterlist = dll.DoublyLinkedList() # O(n) space

	for i in linkedlist: # O(n) time
		if i.value < x:
			lesslist.insert(i.value, 0)
		elif i.value == x:
			lesslist.append(i.value)
		else:
			greaterlist.append(i.value)

	if greaterlist.head:
		if lesslist.tail:
			lesslist.tail.next = greaterlist.head
			greaterlist.head.prev = lesslist.tail
			lesslist.tail = greaterlist.tail
		else: 
			lesslist.head = greaterlist.head
			lesslist.tail = greaterlist.tail

		greaterlist.head = None
		greaterlist.tail = None
		del(greaterlist)

	return lesslist # O(n) time and space

def partitionbetter(linkedlist, x): # For doubly linked list
	midNode = None
	node = linkedlist.head
	while node: # O(n) time
		if node.value < x:
			if node != linkedlist.head:
				nodetomove = node
				node = node.next

				nodetomove.prev.next = nodetomove.next
				if nodetomove.next:
					nodetomove.next.prev = nodetomove.prev
				else:
					linkedlist.tail = nodetomove.prev

				headnode = linkedlist.head
				nodetomove.prev = None
				nodetomove.next = headnode
				headnode.prev = nodetomove
				linkedlist.head = nodetomove
			else:
				node = node.next
		elif node.value == x:
			if midNode:
				nodetomove = node
				node = node.next

				nodetomove.prev.next = node
				if node:
					node.prev = nodetomove.prev
				else:
					linkedlist.tail = nodetomove.prev

				if midNode.prev:
					midNode.prev.next = nodetomove
				else:
					linkedlist.head = nodetomove
				midNode.prev = nodetomove
				nodetomove.prev = midNode.prev
				nodetomove.next = midNode 
			else:
				midNode = node
				node = node.next
		else:
			if not midNode:
				midNode = node
				
			node = node.next # O(n) time and O(1) space

# print([x.value for x in doublylist])
# print([x.value for x in partition(doublylist, 20)])
# partitionbetter(doublylist, 15)
# print([x.value for x in doublylist])

def partitionsingly(linkedlist, x): # For singly list
	node = linkedlist.head
	while node:
		prevNode = node
		node = node.next

		if node and node.value < x:
			nodetomove = node
			node = prevNode

			prevNode.next = nodetomove.next
			nodetomove.next = linkedlist.head
			linkedlist.head = nodetomove # O(n) time and O(1) space


# print([x.value for x in singlylist])
# partitionsingly(singlylist, 30)
# print([x.value for x in singlylist])


#4 You have two numbers represented by a linkedlist, where each node contains a single digit. The digits are stored in reverse order
# such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked
# list

def sumofnumbers_reverselist_reversedreturn(list1, list2): # Doesn't take care of negative numbers
	sumlist = sll.SinglyLinkedList() # O(n) space

	node_list1 = list1.head
	node_list2 = list2.head

	carry = 0
	while node_list1 or node_list2: # O(n) time

		if node_list1 and node_list2:
			nth_sum = node_list1.value + node_list2.value
			node_list1 = node_list1.next
			node_list2 = node_list2.next
		elif node_list1:
			nth_sum = node_list1.value
			node_list1 = node_list1.next
		else:
			nth_sum = node_list2.value
			node_list2 = node_list2.next

		nth_sum += carry
		sumlist.append(nth_sum % 10)
		carry = nth_sum//10

	if carry: sumlist.append(carry)

	return sumlist # O(n) time and space. Returned sum is reversed

def sumofnumbers_reverselist_normalreturn(list1, list2): # Doesn't handle negative numbers
	sumlist = sll.SinglyLinkedList() # O(n) space

	node_list1 = list1.head
	node_list2 = list2.head

	carry = 0
	while node_list1 or node_list2: # O(n) time
	
		if node_list1 and node_list2:
			nth_sum = node_list1.value + node_list2.value
			node_list1 = node_list1.next
			node_list2 = node_list2.next
		elif node_list1:
			nth_sum = node_list1.value
			node_list1 = node_list1.next
		else:
			nth_sum = node_list2.value
			node_list2 = node_list2.next

		nth_sum += carry
		sumlist.insert(nth_sum % 10, 0)
		carry = nth_sum//10

	if carry: sumlist.insert(carry, 0)

	return sumlist # O(n) time and space. Returned sum is order

def sumofnumbers_reverselist_normaldreturn_handlenegative(list1, list2): # Takes care of negative numbers
	sumlist = sll.SinglyLinkedList() # O(n) space

	node_list1 = list1.head
	node_list2 = list2.head

	is1_negative = False
	is2_negative = False
	issum_negative = False
	borrow = False # For subtraction
	carry = 0 # For addition

	if list1.tail:
		is1_negative = list1.tail.value < 0
		if is1_negative: list1.tail.value *= -1
	if list2.tail:
		is2_negative = list2.tail.value < 0
		if is2_negative: list2.tail.value *= -1

	issum_negative = is1_negative 

	while node_list1 or node_list2: # O(n) time

		if is1_negative and is2_negative or not is1_negative and not is2_negative:

			if node_list1 and node_list2:
				nth_sum = node_list1.value + node_list2.value
				node_list1 = node_list1.next
				node_list2 = node_list2.next
			elif node_list1:
				nth_sum = node_list1.value 
				node_list1 = node_list1.next
			else:
				nth_sum = node_list2.value
				node_list2 = node_list2.next

			nth_sum += carry
			sumlist.insert(nth_sum % 10, 0)
			carry = nth_sum//10

		else:
			if node_list1 and node_list2:
				nth_sum = node_list1.value - node_list2.value
				if borrow:
					nth_sum -= 1
					borrow = False

				if nth_sum < 0:
					nth_sum = 10 + node_list1.value - node_list2.value
					borrow = True

				if node_list1.next == None and borrow:
					node_list1 = list2.head
					node_list2 = list1.head

					issum_negative = is2_negative 
					sumlist.clear()
					borrow = False
					continue

				else:
					node_list1 = node_list1.next
					node_list2 = node_list2.next

			elif node_list1:
				nth_sum = node_list1.value
				if borrow:
					nth_sum -= 1
					borrow = False
				node_list1 = node_list1.next
			else:
				node_list1 = list2.head
				node_list2 = list1.head 

				issum_negative = is2_negative 
				sumlist.clear()
				borrow = False
				continue

			sumlist.insert(nth_sum, 0)

	if carry: sumlist.insert(carry, 0) # For addition

	# Triming the zero
	search_node = sumlist.head
	while search_node:
		if search_node.value > 0:
			sumlist.head = search_node
			break

		search_node = search_node.next

	# Assigning negative value to sum
	if issum_negative and sumlist.head:
		sumlist.head.value *= -1

	return sumlist # O(n) time and space. Returned sum is order

def sumofnumbers_normallist_normalreturn_DLL(list1, list2): # Doesn't take care of negative numbers
	sumlist = dll.DoublyLinkedList() # O(n) space

	node_list1 = list1.tail
	node_list2 = list2.tail

	carry = 0
	while node_list1 or node_list2: # O(n) time

		if node_list1 and node_list2:
			nth_sum = node_list1.value + node_list2.value
			node_list1 = node_list1.prev
			node_list2 = node_list2.prev
		elif node_list1:
			nth_sum = node_list1.value
			node_list1 = node_list1.prev
		else:
			nth_sum = node_list2.value
			node_list2 = node_list2.prev

		nth_sum += carry
		sumlist.insert(nth_sum % 10, 0)
		carry = nth_sum//10

	if carry: sumlist.insert(carry, 0)

	return sumlist # O(n) time and space. Returned sum is order

def sumofnumbers_reverselist_normalreturn_recursive_SLL(list1, list2, sumlist, carry):
	if list1.head and list2.head:
		nth_sum = carry + list1.head.value + list2.head.value
	elif list1.head:
		nth_sum = carry + list1.head.value
	else:
		nth_sum = carry + list2.head.valu

	if list1.head.next == None and list2.head.next == None:
		if nth_sum >= 10:
			nth_sum -= 10
			sumlist.insert(nth_sum, 0)
			sumlist.insert(1, 0)
		else:
			sumlist.insert(nth_sum, 0)
	else:
		carry = 0
		if nth_sum >= 10:
			nth_sum -= 10
			sumlist.insert(nth_sum, 0)
			carry = 1
		else:
			sumlist.insert(nth_sum, 0)

		if list1.head: list1.head = list1.head.next
		if list2.head: list2.head = list2.head.next
		sumofnumbers_reverselist_normalreturn_recursive_SLL(list1, list2, sumlist, carry) # O(n) time and space


def sumofnumbers_normallist_normalreturn_recursive_SLL(list1, list2, sumlist): # Doesn't take care of negative numbers
	if not list1.head.next:
		nth_sum = list1.head.value + list2.head.value
		if nth_sum >= 10:
			nth_sum -= 10
			sumlist.insert(nth_sum, 0)
			return 1
		else:
			sumlist.insert(nth_sum, 0)
			return 0
	else:
		nth1_node = list1.head
		nth2_node = list2.head

		list1.head = list1.head.next
		list2.head = list2.head.next
		remainder = sumofnumbers_normallist_normalreturn_recursive_SLL(list1, list2, sumlist) # O(n) time and O(n) space

		nth_sum = nth1_node.value + nth2_node.value + remainder
		if nth_sum >= 10:
			nth_sum -= 10
			sumlist.insert(nth_sum, 0)

			if nth1_node.prev:
				return 1
			else:
				sumlist.insert(1, 0)
		else:
			sumlist.insert(nth_sum, 0)
			if nth1_node.prev:
				return 0

def sumofnumbers_normallist_normalreturn_SLL(list1, list2): # Handles negative numbers
	list1.reverse()
	list2.reverse()
	return sumofnumbers_reverselist_normaldreturn_handlenegative(list1, list2)

# list1 = gensll(5, 0, 9)
# list2 = gensll(5, 0, 9)
# # list1.head.value *= -1

# print("List1:", [x.value for x in list1])
# print("List2:", [x.value for x in list2])
# print("Sum:", [x.value for x in sumofnumbers_normallist_normalreturn_SLL(list1, list2)])
# sumlist = sll.SinglyLinkedList()
# sumofnumbers_reverselist_normalreturn_recursive_SLL(list1, list2, sumlist, 0)
# print("Sum:", [x.value for x in sumlist])




#5 Given two (singly) linked lists, determine if the two list intersect. Return the intersecting node.
#  Note that the intersection is defined based on reference, not values.

# A problem with intersecting singly linked list is that when adjustment is made to the intersecting part of one list,
# it affects the others in ways the others might not be able to control. E.g, if element is poped from one list or appending to 
# one list, the other also have the same element poped/appended, but the "tail pointer" or the "size variable" will be unaware of this
# and thus have the wrong values.

# DOUBLY LINKED LIST CAN'T HAVE INTERSECTING NODES, WITH THE DEFINITION OF INTERSECTION GIVEN IN THIS QUESTION 

def isIntersecting(list1, list2):
	if list1.tail is not list2.tail: # Use is to compare memory locations 
		return None
	
	len_diff = 0
	if len(list1) == len(list2):
		node1 = list1.head 
		node2 = list2.head
	elif len(list1) > len(list2):
		node1 = list1.head
		node2 = None
		len_diff = len(list1) - len(list2)
	else:
		node1 = None
		node2 = list2.head
		len_diff = len(list2) - len(list1)

	while node1  or node2:
		if node1 is node2: return node1

		if node1: node1 = node1.next
		if node2: node2 = node2.next

		len_diff -= 1
		if len_diff == 0:
			if not node1: node1 = list1.head
			if not node2: node2 = list2.head

def isIntersecting_video(list1, list2):
	if list1.tail is not list2.tail:
		return None

	if len(list1) >= len(list2): 
		longer = list1
		shorter = list2
	else:
		longer = list2
		shorter = list1

	longer_node = longer.head
	shorter_node = shorter.head

	len_diff = len(longer) - len(shorter)
	for i in range(len_diff):
		longer_node = longer_node.next

	while longer_node is not shorter_node:
		longer_node = longer_node.next
		shorter_node = shorter_node.next

	return longer_node

# list1 = gensll(15, 0, 9)
# list2 = intersect(list1, 7, 0, 9)
# print("List1:", [x.value for x in list1])
# print("List2:", [x.value for x in list2])
# node = isIntersecting_video(list1, list2)
# value = None
# if node: value = node.value
# print("Intersecting node value:", value)