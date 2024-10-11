# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Example 1:
                
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2

from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left 
        self.right = right 

    def listToTree(self, arr):
        if not arr: 
            return None 
        
        def insertLevelOrder(arr, root, i, n):
            if i < n:
                if arr[i] is None: 
                    return None 
                
                temp = TreeNode(arr[i])
                root = temp 

                root.left = insertLevelOrder(arr, root.left , 2 * i + 1, n)
                root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)

            return root
        
        return insertLevelOrder(arr, None, 0, len(arr))

    def printTree(self, root):
        if not root:
            return
        
        # Level order traversal using a queue
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                print(node.val, end=' ')
                queue.append(node.left)
                queue.append(node.right)
            else:
                print("None", end=' ')
        print()
         


solution = TreeNode()
root = [3,9,20,None,None,15,7]
BinaryTree = solution.listToTree(root)
solution.printTree(BinaryTree)


