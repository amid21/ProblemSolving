# Validate Parentheses
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# Example 1:

# Input: s = "[]"

# Output: true
# Example 2:

# Input: s = "([{}])"

# Output: true
# Example 3:

# Input: s = "[(])"

# Output: false
# Explanation: The brackets are not closed in the correct order.

# Understand
# Complexity (time/space)
# Empty Sting? True 

# Match  
# Dict )-( , }-{, ]-[
# Stack 

# Plan/Pseducode
# ((())) - true
# ({}) - true
# (){} - true
# ({})[] - true 
# (){}{} - true 
# ({){)} - false 

# Create an empty stack
# Create a dict Dict )-( , }-{, ]-[
# Iterate through the string:
# If element is a opening push to the stack 
# If element is closing pop from teh stack 
# If stack is empty return true
# Else False 

# Implement 

class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    dict = {')': '(', '}':'{',']':'['}
    for element in s:
      if element not in dict:
        stack.append(element)
      elif stack and dict[element] == stack[-1]:
        stack.pop()
      else:
        return False

    if not stack:
      return True
    return False

solution = Solution()
print(solution.isValid("(){}{}"))
