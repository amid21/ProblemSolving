class ListNode: 
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next 
        

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head 

        while curr: 
            next = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next 

        return prev 
    
def print_linked_list(node):
    while node:
        print(node.val, end = "->" if node.next else "\n" )
        node = node.next 

if __name__ == "__main__":      
    list = ListNode(1)
    list.next = ListNode(2)
    list.next.next = ListNode(3)
    list.next.next.next = ListNode(4)

    solution = Solution()
    result = solution.reverseList(list)
    print_linked_list(result)

