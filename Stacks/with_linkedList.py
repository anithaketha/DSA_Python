class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.size == 0:
            print("Stack is empty")
            return None
        popped_element = self.head.data
        self.head = self.head.next
        self.size -= 1
        print(f"Popped element is {popped_element}")
        return popped_element

    def peek(self):
        if self.size == 0:
            print("Stack is empty")
            return None
        print("Peek element is", self.head.data)
        return self.head.data

    def display(self):
        if self.size == 0:
            print("Stack is empty")
        else:
            curr = self.head
            print("Elements in stack:", end=" ")
            while curr:
                print(curr.data, end=" ")
                curr = curr.next
            print()  # Newline for better readability

ll = Linkedlist()
ll.push(1)
ll.push(2)
ll.push(3)
ll.pop()  # Removes 3
ll.peek()  # Should print 2
ll.display()  # Should display 2 1
