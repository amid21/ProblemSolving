from typing import Optional
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, l: ListNode):
        curr = l
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next 
        return prev 
    
    def print_linked_list(self, node: ListNode):
        while node:
            print(node.val, end = "->" if node.next else "\n")
            node = node.next
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = solution.reverseList(l1)
        l2 = solution.reverseList(l2) 
        carry = 0 
        curVal = 0 
        dummy = ListNode()
        current = dummy
        while l1 or l2: 
            curVal = carry
            if l1:
                curVal += l1.val  
                l1 = l1.next
            
            if l2: 
                curVal += l2.val
                l2 = l2.next 
            
            carry = curVal // 10 
            curVal %= 10

            current = ListNode(curVal)
            current = current.next

        
            
            
        return current.next
        



l1 = ListNode(2)
l1.next = ListNode(3)
l1.next.next = ListNode(4)

l2 = ListNode(4)
l2.next = ListNode(6)
l2.next.next = ListNode(7)

solution = Solution()
result = solution.addTwoNumbers(l1, l2)
pResult = solution.print_linked_list(result)
