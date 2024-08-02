class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, x: int) -> None:
        # Push element onto the primary stack
        self.stack.append(x)
        
        # Push the minimum value onto the min stack
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    
    def pop(self) -> None:
        if self.stack:
            # Pop element from the primary stack
            top = self.stack.pop()
            
            # Pop the top element from the min stack if it's the current minimum
            if self.min_stack and top == self.min_stack[-1]:
                self.min_stack.pop()
    
    def getMin(self) -> int:
        # Return the top element from the min stack, which is the current minimum
        if self.min_stack:
            return self.min_stack[-1]
        return None

# Example usage
min_stack = MinStack()
min_stack.push(3)
min_stack.push(5)
print(min_stack.getMin())  # Output: 3
min_stack.push(2)
min_stack.push(1)
print(min_stack.getMin())  # Output: 1
min_stack.pop()
print(min_stack.getMin())  # Output: 2
min_stack.pop()
print(min_stack.getMin())  # Output: 3
