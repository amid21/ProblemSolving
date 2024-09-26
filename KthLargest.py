import heapq
from typing import List
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while (len(self.heap) > self.k):
            heapq.heappop(self.heap)
    
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if (len(self.heap) > self.k):
            heapq.heappop(self.heap)
    
        return self.heap[0]

# Testing the KthLargest class
if __name__ == "__main__":
    # Example: k = 3, nums = [4, 5, 8, 2]
    k = 3
    nums = [4, 5, 8, 2]
    
    # Instantiate KthLargest object
    obj = KthLargest(k, nums)
    
    # Testing the add method
    print(obj.add(3))  # Expected output: 4
    print(obj.add(5))  # Expected output: 5
    print(obj.add(10)) # Expected output: 5
    print(obj.add(9))  # Expected output: 8
    print(obj.add(4))  # Expected output: 8