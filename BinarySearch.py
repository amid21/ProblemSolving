class Solution:
    def BinarySearch(self, nums, target):
        r = len(nums) - 1
        l = 0 

        while l <= r: 
            m = (l + r) // 2
            if nums[m] == target: 
                return m 
            elif nums[m] > target: 
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        return -1 
        
        # l = len(nums)
        # m = int(l/2)
        # for  i in range(l):
        #     if nums[m] == target:
        #         return m
        #     elif nums[m] > target: 
        #         l = m
        #         m = int(m/2)
        #     elif nums[m] < target: 
        #         i = m
        #         m = int((l + i) / 2)
        
        # return -1
        




#nums = list(map(int, input("Enter array: ").split()))
nums = [int(x) for x in input("Enter array: ").split()]
target = int(input("Enter target: "))

solution = Solution()
print(solution.BinarySearch(nums, target))
