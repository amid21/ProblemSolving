from typing import List
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if x != y: 
                heapq.heappush(stones, -(y-x))
        
        if not stones:
            return 0
        return -(stones[0])


solution = Solution()
stones = [2, 2, 2]
result = solution.lastStoneWeight(stones)
print(result)
