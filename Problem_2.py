# Problem 1: Contains Duplicates
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Understand:
# What if the array is empty? Return false

# Match:
# Hashmap

# Plan:
# We create a hashmap and put all unique values we see as keys and the number of times we see each value as the value for that key. Return true if any value greater than 1 else false

def duplicate_Present(nums):
  dict = {}
  for num in nums:
    if num in dict:
      return True
    else:
      dict[num] = 1 
  return False


nums = [1,2,2,3,4]
print(duplicate_Present(nums))

# Problem 2: Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input:  slicing to obtain the rows with the index 3 through 5 in
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# Understand:
# Time complexity? 
# Do the indices have to be next to each other? No
# what if there were two sets of numbers that returns the target when added ?

#Example: [2, 11, 7, 15], target = 9
# 1)  9-2=7


# Match: 
# Dict/Hashmap
# Nested for-loop
# subtract from target current element and if the result is present in the dict, then we can select those indices


# Plan:

def sum_two(nums, target):
  for i in range(len(nums)):
    temp = nums[i]
    nums[i] = -1
    if (target-temp in nums):
      return [i, nums.index(target-temp)]
    nums[i] = temp
  return []

nums = [3, 5]
target = 8
print(sum_two(nums,target))

