# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

# Example 1:

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

#[-2, 0, 3, -5, 2, -1]
#[-2, -2, 1, -4, -2, -3] - prefixSum 

# Can there be no range given? 
# There will be a range always given 
# [[0, 2, -2, 3]], [0, 1], [2, 2], [0, 3]]
# [null, 2, -2, 3]

# [0, 2, 0, 3]
# [null, ps[r] - p[i-1] ]
class NumArray:

    def __init__(self, nums):
        self.nums = nums 
        self.prefixSum = []
        s = 0
        for i in range(len(self.nums)):
            s += self.nums[i]
            self.prefixSum.append(s)

#[0, 2, -2, 3] - nums
# [0, 2, 0, 3] - prefixSum
# 3 - 3 = 0 - output

    def sumRange(self, left, right):
        if left > 0:
            return self.prefixSum[right] - self.prefixSum[left-1] 
        else:
            return self.prefixSum[right]

solution = NumArray([-2, 0, 3, -5, 2, -1])
print(solution.sumRange(0, 3))
print(solution.sumRange(1, 3))