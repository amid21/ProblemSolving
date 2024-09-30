class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next

class Solution:
    def mergeTwoLists(self, List1: ListNode, List2:ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy 

        while List1 and List2:
            if List1.val < List2.val: 
                current.next = List1 
                List1 = List1.next
            else:
                current.next = List2
                List2 = List2.next
            current = current.next 
        
        if List1:
            current.next = List1

        if List2: 
            current.next = List2 
        
        return dummy.next
    
# Helper function to print the linked list
def print_linked_list(node):
    while node: 
        print(node.val, end = "->" if node.next else "\n")
        node = node.next

if __name__ == "__main__":
    # Manually creating the first linked list: 1 -> 2 -> 4
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    
    # Manually creating the second linked list: 1 -> 3 -> 4
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    
    # Merge the two linked lists
    solution = Solution()
    merged_list = solution.mergeTwoLists(list1, list2)
    
    # Print the merged linked list
    print("Merged list:")
    print_linked_list(merged_list)
