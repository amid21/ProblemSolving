# Merge Two Sorted Linked Lists
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

# The new list should be made up of nodes from list1 and list2.

# Example 1:

# Input: list1 = [1,2,4], list2 = [1,3,5]

# Output: [1,1,2,3,4,5]
# Example 2:

# Input: list1 = [], list2 = [1,2]

# Output: [1,2]
# Example 3:

# Input: list1 = [], list2 = []

# Output: []

# Understand
# Complexity 
# Linked list is sorted, one can be empty or both can be empty

# Match 
# No need for new ds, use pointers

# Plan/Pseudocode 
# Start with the head of list1 
# Create a dummy node
# if head of list1 is <= head of list2 
# point head of list2 to head of list1 
# 

# Implement 
class Node:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
  def mergeTwoLists(self, list1, list2):

    dummy = Node()
    node = dummy


    while list1 and list2: 
      if list1.val < list2.val:
        node.next = list1
        list1 = list1.next
      else:
        node.next = list2
        list2 = list2.next 
      node = node.next

    if list1 is not None:
      node.next = list1 
    else:
      node.next = list2 

    return dummy.next 

list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(3)
list1.next.next.next = Node(4)

list2 = Node(1)
list2.next = Node(2)
list2.next.next = Node(3)
list2.next.next.next = Node(4)
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# def print_list(node):
#   while node:
#       print(node.val, end=" -> " if node.next else "\n")
#       node = node.next

def linked_list_to_list(node):
  result = []
  while node:
      result.append(node.val)
      node = node.next
  return result

merged_list_as_list = linked_list_to_list(solution.mergeTwoLists(list1, list2))
print(merged_list_as_list)






