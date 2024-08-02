class Queue:
    def _init_(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if not self.isempty():
            return self.items.pop(0)
        else:
            raise IndexError("Dequeue from an empty queue")

    def isempty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def peek(self):
        """Return the item at the front of the queue without removing it."""
        if not self.isempty():
            return self.items[0]
        else:
            raise IndexError("Peek from an empty queue")

# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Output: 1
print(queue.peek())     # Output: 2
print(queue.size())     # Output: 2
print(queue.isempty()) # Output: False
queue.dequeue()
queue.dequeue()
print(queue.isempty()) # Output: True