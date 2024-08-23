# Linked List Cycle Detection
# Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

# There is a cycle in a linked list if at least one node in the list that can be visited again by following the next pointer.

# Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

# Note: index is not given to you as a parameter.

# Example 1:



# Input: head = [1,2,3,4], index = 1

# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:



# Input: head = [1,2], index = -1

# Output: false

# understand
# we are trying to find if the LL is a cycle
# the index is the index of what the tail is pointing to
# what if the LL is empty -> not cycle
# time complexity & space complexity?
# if its a cycle then return true, if its not return false

# match
# linked list

# plan/ pseudocode
# 2 pointers
# 1 fast pointer and 1 slow pointer
# they both start at the head and the slow pointer increments by 1 and the fast pointer increments by 2
# if the 2 pointers are ever equal to each other than we know it is a cycle
# if they are never equal to each other and we are out of the list then we know its not a cycle
# example
# [1,2,3,4]
# slow = 0, 1, 2, 3
# fast = 0, 2, 1, 3

# [3, 2, 7, 11, 9]  
# slow = 0, 1, 2, 3
# fast = 0, 2, 4, 
class Node:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
  def hasCycle(self, head) -> bool:
    slow, fast = head, head

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        return True
    return False

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

solution = Solution()
# print(solution.hasCycle(head))

head.next.next.next.next = head.next

print(solution.hasCycle(head))

# Time Complexity O(n)
# Space Complexity O(1)
