# Buy and Sell Crypto
# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

# Example 1:

# Input: prices = [10,1,5,6,7,1]

# Output: 6
# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

# Example 2:

# Input: prices = [10,8,7,5,2]

# Output: 0
# Explanation: No profitable transactions can be made, thus the max profit is 0.

# ________________________________________________________________________________

# Understand
# we are trying to find the greatest diff between 2 of the prices. Lower should always come first
# we are going to return the diff of the prices
# If array empty then return 0
# If all the nums are the same then return 0
# If the diff is less than 0 return 0
# what is the time and space complexity

# Match
# Use the array they give
# two painter

# Plan/Pseudocode 
# have a min pointer and a max pointer 
# start both of them at the first element
# check to see if the next element is greater or less than the current one
# if it is less than, we will move both of them over
# if it is greater than we only move the max pointer
# We check the diff between the 2 pointers and store them in a variable & update if we find something of 
# greater diff
# return the diff

# Implement
class Solution:
  def maxProfit(self, prices) -> int:
    L = 0
    r = 1
    big = 0
    while r < len(prices):
      if prices[r] - prices[L] > 0:
        diff = prices[r] - prices[L]
        big = max(big, diff)
      else:
        L = r
      r += 1
    return big


solution = Solution()
print(solution.maxProfit([10,1,5,6,7,1]))

# Review
#           l  r 
# 10,1,5,6,7,1
# diff = 6
# big = 6

# Evaluate 
# Time/Space O(n)
