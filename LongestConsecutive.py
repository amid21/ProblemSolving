class Solution:
    def longestConsecutive(self, nums) -> int:
        longestSteak = 0 
        hashSet = set(nums)
        for num in hashSet: 
            if num - 1 not in hashSet: 
                currentStreak = 1
                currentNum = num 
                while currentNum + 1 in hashSet:
                    currentStreak+=1
                    currentNum+=1
                longestSteak = max(longestSteak, currentStreak)
        return longestSteak

solution = Solution()
print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
