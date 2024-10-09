class ListNode: 
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution: 
    def pairSum(self, head): 
        slow = head 
        fast = head 
        maxVal = 0
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 

        curr = slow 
        prev = None 

        while curr: 
            curr.next, prev, curr = prev, curr, curr.next 
        
        while prev: 
            maxVal = max(maxVal, head.val + prev.val)
            head = head.next
            prev = prev.next 
        
        return maxVal
    def print_linked_list(self, head):
        while head: 
            print(head.val, end=" -> " if head.next else "\n")
            head = head.next 
            
arr = [int(x) for x in input("Enter ll: ").split()]
print(arr)
head = ListNode(arr[0])
current = head
for i in range(1, len(arr)):
   current.next = ListNode(arr[i])
   current = current.next 
# head = ListNode(3)
# head.next = ListNode(4)
# head.next.next = ListNode(5)


solution = Solution()
res = solution.pairSum(head)
print(res)
#olution.print_linked_list(res)

