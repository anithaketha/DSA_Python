class Stack:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.stack=[]
    def push(self,item):
        if len(self.stack)>=self.maxsize :
            print("Stack is full")
        else:
            self.stack.append(item)
    def pop(self):
        if not self.empty():
            pop_el=self.stack.pop()
            print(f"popped element is {pop_el}")
            return pop_el
        else:
            print("Stack is empty")
            return None
    def peek(self):
        top_el=self.stack[-1]
        print(f"peek element is {top_el}")
        return top_el
    def empty(self):
        return len(self.stack)==0
    def display(self):
        if not self.empty():
            print("stack is ",self.stack)
        else:
            print("Stack is empty")
stack=Stack(6)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.pop()
stack.push(6)
stack.peek()
stack.display()