# Two Integer Sum
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:

# Input: nums = [4,5,6], target = 10
# Output: [0,2]

# Example 3:

# Input: nums = [5,5], target = 10
# Output: [0,1]

#_______________________________________________________________

# Understand 
# Time Complexity, Space Complexity 

# Match
# dictionary
# list

# Plan/Pseudocode
# difference between the target and the number in the array
# look for that difference in the dict, if its there than find its index and return
# the index of that number and the number from the array
# if the difference is not there I want to add both the number and its index it into the dict

#Implement 

class Solution:
  def twoSum(self, nums, target):
    dict = {}
    for i, j in enumerate(nums):
      diff = target - j
      if diff in dict:
        return [dict[diff], i]
      dict[j] = i

solution = Solution()

print(solution.twoSum([5,5,5,4,4,5,6,7 ], 13))

#Review 



# dict = {}
# n = [1, 2, 3]
# for i, j in enumerate(n):
#   print(i, j)

