class ListNode:
    def __init__(self, val=0, next = None): 
        self.val = val 
        self.next = next 
    
class Solution:
    def RemoveDuplicates(self, head: ListNode) -> ListNode:
        prev = curr = head 

        while curr: 
            while curr and prev.val == curr.val:
                curr = curr.next
            prev.next = curr

            prev = curr
        
        return head 
    
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)

solution = Solution()
new_head = solution.RemoveDuplicates(head)

current = new_head
while current:
    print(current.val, end = "->" if current.next else "\n")
    current = current.next 

