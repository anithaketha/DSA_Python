class QueueWithStacks:
    def __init__(self):
        self.stack1 = []  
        self.stack2 = [] 

    def enqueue(self, item):
        
        self.stack1.append(item)

    def dequeue(self):
    
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
    
        return self.stack2.pop()

    def is_empty(self):
       
        return not self.stack1 and not self.stack2

    def peek(self):
       
        if self.stack2:
            return self.stack2[-1]
        
  
        if self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            print("peek from an empty queue")
        
        return self.stack2[-1]

queue = QueueWithStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  
print(queue.peek())    
print(queue.is_empty()) 
