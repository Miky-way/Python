from stack_withlist import Stack as stack_l
from stack_withlinkedlist import Stack as stack_ll


print("\n ---------------------------List------------------------------------\n")
stack1 = stack_l(10)
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)
print(stack1)
print(stack1.peek())
print(stack1.pop())
print(stack1)

print("List capacity", stack1.capacity)


print("\n\n------------------------------------Linked list-------------------------------\n")
stack2 = stack_ll()
stack2.push(1)
stack2.push(2)
stack2.push(3)
stack2.push(4)
stack2.push(5)
print(stack2)
print(stack2.peek())
print(stack2.pop())
print(stack2)