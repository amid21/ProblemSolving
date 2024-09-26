class Solution:
    def isValid(self, s: str) -> bool:
        # create a dict to math open with close 
        # create an empty stack 
        # iterate through elements of the string 
        # if it is open par we will add to stack 
        # if it is closing par we will remove from stack 
        # if stack is emplty 
        # return true
        # else return false 
        dict = {'}':'{', ']':'[', ')':'('}
        openSet = {'{', '(', '['}
        stack = []
        for element in s: 
            if element in openSet:
                stack.append(element)
            elif stack and dict[element] == stack[-1]:
                stack.pop()
        if stack: 
            return False
        return True
solution = Solution()
print(solution.isValid("()[]{}"))


