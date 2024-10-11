class Solution:
    def findMin(self, nums) -> int:
        # Initialize left and right pointers
        l, r = 0, len(nums) - 1

        # While left pointer is less than right pointer we have not exhausted the possible numbers
        while l < r:
            # Get the mid point of the two pointers 
            mid = (l + r) // 2

            # Check if mid point is less than or greater than the right pointer
            if nums[mid] > nums[r]:
                # If mid point is greater than the right pointer, then the smaller half is the right half. Set the left pointer to mid pointer + 1.
                l = mid + 1
            else:
                # If mid pointer is less than the right pointer, then the smaller half is the left half. Set the right pointer to the mid pointer
                r = mid
        
        # Return number at right pointer for smallest number in list 
        return nums[r]


solution = Solution()
arr = [int(x) for x in input("Enter: ").split()]
result = solution.findMin(arr)
print(result)