from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()
            if x != y:    
                stones.append(y-x)
                stones.sort()
        if not stones:
            return 0
        return stones[-1]


solution = Solution()
stones = []
result = solution.lastStoneWeight(stones)
print(result)
