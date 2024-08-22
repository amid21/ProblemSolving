# Is Palindrome
# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Example 1:

# Input: s = "Was it a car or a cat I saw?"

# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

# Example 2:

# Input: s = "tab a cat"

# Output: false
# Explanation: "tabacat" is not a palindrome.

# Constraints:

# 1 <= s.length <= 1000
# s is made up of only printable ASCII characters.

# Understand 
# Complexity, W=w

# Match
# Two pointer solution 

# Plan/Pseudocode
# while loop until left pointer < right pointer - have one pointer in the beginning and one pointer at end of the string.
# Check if either of chars is a non-alphanumeric - if is move a pointer;
# If not compare them - if they are the same move both pointer;
# If they are different - return
# return true outside of the loop. 

# Implement 
class Solution:
  def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    leftp = 0 
    rightp = len(s) - 1    
    while leftp <= rightp:
      while leftp <= rightp and not s[leftp].isalnum():
        leftp+=1
      while leftp <= rightp and not s[rightp].isalnum():
        rightp-=1    
      if s[leftp]==s[rightp]:
        leftp+=1
        rightp-=1
      else:
        return False
    return True

solution = Solution()

print(solution.isPalindrome("Was it a car or a cat I saw?"))

# c.isalnum()
# original_string = "Hello, World!"
# lowercase_string = original_string.lower()
# print(lowercase_string)
# class Solution:
#   def isPalindrome(self, s: str) -> bool:
#       s = s.lower()
#       leftp = 0
#       rightp = len(s) - 1
#       while leftp <= rightp:
#           while leftp <= rightp and not s[leftp].isalnum():
#               leftp += 1
#           while leftp <= rightp and not s[rightp].isalnum():
#               rightp -= 1
#           if leftp <= rightp and s[leftp] != s[rightp]:
#               return False
#           leftp += 1
#           rightp -= 1
#       return True

# solution = Solution()
# print(solution.isPalindrome("Was it a car or a cat I saw"))  # Output should be True
