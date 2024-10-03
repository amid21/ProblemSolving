
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1 = m - 1
        index2 = n - 1
        insertIndex = m + n - 1 
        
        while index2 >= 0:
            if index1>=0 and nums2[index2] >= nums1[index1]:
                nums1[insertIndex] = nums2[index2]
                index2-=1
                insertIndex-=1
            else:
                nums1[insertIndex] = nums1[index1]
                index1-=1
                insertIndex-=1
            


        print(nums1)


solution = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6] 
n = 3
solution.merge(nums1, m, nums2, n)
