# Queue
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]
    
    def size(self):
        return len(self.queue)

print("Queue Operations:")
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue after enqueues:", queue.queue)
print("Dequeue:", queue.dequeue())
print("Queue after dequeue:", queue.queue)
print("Peek:", queue.peek())
print("Is queue empty?", queue.is_empty())
print("Queue size:", queue.size())
print()


# Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def delete_node(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next
        if current is None:
            return "Node not found"
        previous.next = current.next
    
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

print("Linked List Operations:")
linked_list = LinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)
print("Linked List after insertions:")
linked_list.traverse()
linked_list.delete_node(20)
print("Linked List after deleting 20:")
linked_list.traverse()
linked_list.delete_node(100)  # Trying to delete a non-existent element
linked_list.traverse()
print()


# Stack
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

print("Stack Operations:")
stack = Stack()
stack.push("a")
stack.push("b")
stack.push("c")
print("Stack after pushes:", stack.stack)
print("Pop:", stack.pop())
print("Stack after pop:", stack.stack)
print("Peek:", stack.peek())
print("Is stack empty?", stack.is_empty())
print("Stack size:", stack.size())
print()


# Array
class Array:
    def __init__(self):
        self.array = []
    
    def append(self, item):
        self.array.append(item)
    
    def pop(self):
        if self.is_empty():
            return "Array is empty"
        return self.array.pop()
    
    def insert(self, index, item):
        if index >= len(self.array):
            self.array.append(item)
        else:
            self.array = self.array[:index] + [item] + self.array[index:]
    
    def remove(self, item):
        for i in range(len(self.array)):
            if self.array[i] == item:
                self.array = self.array[:i] + self.array[i+1:]
                return
        print("Item not found")
    
    def is_empty(self):
        return len(self.array) == 0
    
    def display(self):
        print(self.array)



array = Array()
array.append(5)
array.append(10)
array.append(15)
print("Array after appends:", array.array)
array.insert(1, 7)
print("Array after inserting 7 at index 1:", array.array)
array.remove(10)
print("Array after removing 10:", array.array)
array.pop()
print("Array after pop:", array.array)
print("Is array empty?", array.is_empty())
print("Final array:")
array.display()

