# STACK AND QUEUE INTERVIEW QUESTIONS

# Question 1: Describe how you can use a single python list to implement k number of stack
# I should be given the capacity of the list
from stack_withsharedlist import Stack as stack_wsl

def multiStack(capacity, k):
	width = capacity // k
	stacks = []
	sharedlist = [None] * 39

	counter = 0
	while counter < capacity:
		start = counter
		end = counter + width - 1

		if end + width >= capacity:
			end += capacity - end - 1
			counter = capacity

		stack = stack_wsl(sharedlist, start, end)
		stack.push(1)
		stack.push(2)
		stack.push(3)
		stack.push(4)
		stack.push(5)
		stacks.append(stack) 
		counter += width

	return stacks, sharedlist

# stacks, sharedlist = multiStack(39, 7)

# print("Popping from stack[0]", stacks[0].pop())
# print("Popping from stack[5]", stacks[5].pop())
# print("Popping from stack[3]", stacks[3].pop())
# print("Popping from stack[5]", stacks[5].pop())
# print("Popping from stack[3]", stacks[3].pop())
# print("Peeking from stack[4]", stacks[4].peek())
# print("Peeking from stack[2]", stacks[2].peek())

# counter = 0
# for i in stacks:
# 	print("--------------- Stack {} ----------------".format(counter))
# 	counter += 1
# 	print(i)
# 	print("Capacity:", i.capacity())
# 	print("Size:", len(i))
# 	print("\n")


# print("\n\n--------------- Printing everything in sharedlist ----------------")
# for i in sharedlist:
# 	print(i)



# Question 2: Design a stack that in addition to push and pop has also function min which returns the min element.
# should all perform in O(1).

from stack_withlinkedlist_andminfunction import Stack as stack_ll
from random import randint

stack1 = stack_ll()
for i in range(10):
	stack1.push(randint(0, 100))
# print(stack1)
# print("Min value is:", stack1.min())
# print("Popping:", stack1.pop())
# print("Popping:", stack1.pop())
# print("Popping:", stack1.pop())
# print("Popping:", stack1.pop())
# print("Popping:", stack1.pop())
# print("Popping:", stack1.pop())
# print(stack1)
# print("New min value is:", stack1.min())




from setofstacks_withlinkedlist import SetOfStacks as sos
from setofstacks_withlinkedlist import PlateStack as ps
from random import randint

# setofstacks = sos(7)
# for i in range(50):
# 	setofstacks.push(randint(0, 100))

# print(setofstacks)
# print("\n")

# print("Popping general:", setofstacks.pop())
# print(setofstacks)
# print("\n")

# print("Peeking:", setofstacks.peek())
# print("Popping general:", setofstacks.pop())
# print(setofstacks)
# print("\n")

# print("Popping substack[3]:", setofstacks.popAt(3))
# print(setofstacks)
# print("\n")

# print("Popping substack[0]:", setofstacks.popAt(0))
# print(setofstacks)
# print("\n")

# print("Popping substack[2]:", setofstacks.popAt(2))
# print(setofstacks)
# print("\n")

# print("Popping substack[3]:", setofstacks.popAt(3))
# print(setofstacks)
# print("\n")

# print("Popping substack[1]:", setofstacks.popAt(1))
# print(setofstacks)
# print("\n")

# print("Popping substack[0]:", setofstacks.popAt(0))
# print(setofstacks)
# print("\n")

# for i in range(10):
# 	setofstacks.push(randint(0, 100))

# print("-------------------- After some pushs --------------------------")
# print(setofstacks)
# print("\n")

# print("Popping substack[5]:", setofstacks.popAt(5))
# print(setofstacks)
# print("\n")

# print("Popping substack[4]:", setofstacks.popAt(4))
# print(setofstacks)
# print("\n")

# print("Popping substack[2]:", setofstacks.popAt(2))
# print(setofstacks)
# print("\n")

# print("Popping general:", setofstacks.pop())
# print(setofstacks)
# print("\n")


# plateStack = ps(7)
# for i in range(50):
# 	plateStack.push(randint(0, 100))

# print(plateStack)
# print("\n")

# print("Popping general:", plateStack.pop())
# print(plateStack)
# print("\n")

# print("Popping general:", plateStack.pop())
# print(plateStack)
# print("\n")

# print("Popping substack[3]:", plateStack.popAt(3))
# print(plateStack)
# print("\n")

# print("Popping substack[2]:", plateStack.popAt(2))
# print(plateStack)
# print("\n")

# print("Popping substack[3]:", plateStack.popAt(3))
# print(plateStack)
# print("\n")

# print("Popping substack[1]:", plateStack.popAt(1))
# print(plateStack)
# print("\n")

# print("Popping substack[3]:", plateStack.popAt(3))
# print(plateStack)
# print("\n")

# print("Popping substack[3]:", plateStack.popAt(3))
# print(plateStack)
# print("\n")

# print("Popping substack[3]:", plateStack.popAt(3))
# print(plateStack)
# print("\n")

# print("Popping substack[3]:", plateStack.popAt(3))
# print(plateStack)
# print("\n")

# print("Popping substack[3]:", plateStack.popAt(3))
# print(plateStack)
# print("\n")

# print("Popping substack[3]:", plateStack.popAt(3))
# print(plateStack)
# print("\n")

# print("Popping substack[1]:", plateStack.popAt(1))
# print(plateStack)
# print("\n")

# print("Popping substack[1]:", plateStack.popAt(1))
# print(plateStack)
# print("\n")

# print("Popping substack[1]:", plateStack.popAt(1))
# print(plateStack)
# print("\n")

# print("Popping substack[1]:", plateStack.popAt(1))
# print(plateStack)
# print("\n")

# print("Popping substack[1]:", plateStack.popAt(1))
# print(plateStack)
# print("\n")

# print("Popping substack[1]:", plateStack.popAt(1))
# print(plateStack)
# print("\n")

# print("Popping substack[1]:", plateStack.popAt(1))
# print(plateStack)
# print("\n")

# print("Popping substack[1]:", plateStack.popAt(1))
# print(plateStack)
# print("\n")

# print("Popping substack[1]:", plateStack.popAt(1))
# print(plateStack)
# print("\n")

# print("Popping substack[1]:", plateStack.popAt(1))
# print(plateStack)
# print("\n")

# print("Popping general:", plateStack.pop())
# print(plateStack)
# print("\n")

# for i in range(10):
# 	plateStack.push(randint(0, 100))

# print("-------------------- After some pushs --------------------------")
# print(plateStack)
# print("\n")

# print("Popping substack[5]:", plateStack.popAt(5))
# print(plateStack)
# print("\n")

# print("Popping substack[4]:", plateStack.popAt(4))
# print(plateStack)
# print("\n")

# print("Popping substack[4]:", plateStack.popAt(4))
# print(plateStack)
# print("\n")

# print("Popping substack[4]:", plateStack.popAt(4))
# print(plateStack)
# print("\n")

# print("Popping substack[4]:", plateStack.popAt(4))
# print(plateStack)
# print("\n")

# print("Popping substack[4]:", plateStack.popAt(4))
# print(plateStack)
# print("\n")

# print("Popping substack[4]:", plateStack.popAt(4))
# print(plateStack)
# print("\n")

# print("Popping substack[4]:", plateStack.popAt(4))
# print(plateStack)
# print("\n")

# print("Popping substack[2]:", plateStack.popAt(2))
# print(plateStack)
# print("\n")

# print("Popping general:", plateStack.pop())
# print(plateStack)
# print("\n")


# Question 4: Implement queue class using two stacks
import queue_with2stacks as queue_w2s

# queue = queue_w2s.Queue()
# for i in range(10):
# 	queue.enqueue(randint(0, 100))

# print(queue)
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.peek())
# print(queue)


# Question 5: An animal shelter which holds only dogs and cats operates on stricktly first in first out basis.
# people must adopt either the oldest (based on arrival time) of all the animals at the shelter, or they can select 
# whether they would prefer a dog or a cat (and will receive the oldest of the selected animal type). Create a data
# structure that maintains this system and implement operations such as enqueue, dequeueAny, dequeueDog, dequeueCat.
import animalshelter

queue = animalshelter.AnimalQueue()
animals = ["Dog", "Cat"]
for i in range(20):
	queue.enqueue(animals[randint(0, 1)])

print(queue)
print("\n-------------------------------------------------------------------------------------\n")
print(queue.dequeueAny())
print(queue.dequeueAny())
print(queue.dequeueCat())
print(queue.dequeueAny())
print(queue.dequeueCat())
print(queue.dequeueDog())
print(queue.dequeueDog())
print(queue.dequeueCat())
print("\n-------------------------------------------------------------------------------------\n")
print(queue)
