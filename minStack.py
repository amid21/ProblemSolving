class MinStack: 
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, item):
        self.stack.append(item)
        if not self.minStack or item <= self.minStack[-1]:
            self.minStack.append(item)

    def pop(self):
        temp = self.stack.pop()
        if temp == self.minStack[-1]:
            self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]
        



solution = MinStack()
# solution.pop()
# solution.push(4)
# solution.push(2)
# solution.push(3)
# solution.push(1)
# solution.pop()
print(solution.stack)
result = solution.top()
print(result)