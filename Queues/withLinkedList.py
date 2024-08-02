class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, x):
        new_node = Node(x)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if self.front is None:
            self.front = new_node
        self.size += 1

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return None
        
        deleted_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        print("Deleted element is", deleted_data)
        return deleted_data

    def peek(self):
        if self.isempty():
            print("Queue is empty")
            return None
        return self.front.data

    def isempty(self):
        return self.size == 0

# Example usage
ll = LinkedList()
ll.enqueue(1)
ll.enqueue(2)
ll.enqueue(3)
ll.dequeue()
peek_element = ll.peek()
if peek_element is not None:
    print("The peek element is", peek_element)
else:
    print("Queue is empty, no peek element")
