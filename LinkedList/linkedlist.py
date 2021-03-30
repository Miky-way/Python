import singlylinkedlist as sll

singlylinkedlist = sll.SinglyLinkedList()

singlylinkedlist.append(1)
singlylinkedlist.insert(0, 0)
singlylinkedlist.insert(2, 2)
singlylinkedlist.append(3)
singlylinkedlist.append("Hello people")

print(singlylinkedlist.aslist())

singlylinkedlist.pop()
print("List after pop():",singlylinkedlist.aslist())
singlylinkedlist.remove(0)
print("List after reomving index 0:",singlylinkedlist.aslist())
singlylinkedlist.remove(1)
print("List after removing index 1:",singlylinkedlist.aslist())
singlylinkedlist.replace(2, 1)
print("List after replace index 1 with 2:",singlylinkedlist.aslist())
singlylinkedlist.insert(3, 0)
print("List after inserting 3 at index 0:",singlylinkedlist.aslist())
singlylinkedlist.replace(0, 0)
print("List after replacing index 0 with 0:",singlylinkedlist.aslist())
singlylinkedlist.append("People")
print("List after appending People:",singlylinkedlist.aslist())
singlylinkedlist.replace(3, 3)
print("List after replacing index 3 with 3:",singlylinkedlist.aslist())
singlylinkedlist.append(["new", "list", "object"])
print("List after appending list:",singlylinkedlist.aslist())


print("Index of list object:", singlylinkedlist.indexof(["new", "list", "object"]))
print("Get value at 4:", singlylinkedlist.get(4))
print("Get value at 2:", singlylinkedlist.get(2))
print("Get value at 0:", singlylinkedlist.get(0))


singlylinkedlist.removeValue(["new", "list", "object"])
print("List after removing by value:",singlylinkedlist.aslist())

print("Size of list =", singlylinkedlist.size())