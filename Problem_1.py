# Duplicate Integer

# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true
# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false

# _________________________________________ 

# Understand 
# Time complexity? Space complexity? 
# What if the list empty? we return false in this case 

# Match 
# set
# dict

# Plan 
# create an empty set
# for loop
# check to see if the element from the array is in the set
# if it is then return True
# if it isnt then add it to the set
# once out of the loop then return false

# Implement
class Solution:
  def hasDuplicate(self, nums) -> bool:
    duplicate = set()
    for i in nums:
      if i in duplicate:
        return True
      else:
        duplicate.add(i)
    return False

solution = Solution()
print(solution.hasDuplicate([1, 2, 3, 3]))
print(solution.hasDuplicate([1, 2, 3, 4]))
# Review 
# Input: nums = [1, 2, 3, 3] Output: True
# Input: nums = [1, 2, 3, 4] Output: False 

# Evaluate 
# Time Complexity: O(n)
# Space Complexity: O(n)