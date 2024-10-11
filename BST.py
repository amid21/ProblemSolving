# Binary Search Tree
# int val 
# return True of val exists in BST else false 

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right 

class Solution: 
    def getBinaryTreeHeight(self, root:TreeNode):
        if root == None:
            return -1
        
        leftHeight = self.getBinaryTreeHeight(root.left)
        rightHeight = self.getBinaryTreeHeight(root.right)

        if leftHeight > rightHeight:
            return leftHeight + 1 
        else:
            return rightHeight + 1 
    
    def printBST(self, root:TreeNode):
        if root:
            result.append(root.val)
            solution.printBST(root.left)
            solution.printBST(root.right)
        return result


    def searchBST(self, root:TreeNode, searchVal:int): 
        # if we have ran out of values to search for return false 
        if (root == None):
            return result 
        
        # if we have found our searchvalue we return true
        elif (root.val == searchVal):
            return solution.printBST(root)
        
        else:
            # if the value is greater than the searchvalue we traverse on the left side of the tree
            if(root.val > searchVal):
                return solution.searchBST(root.left, searchVal)
            else:
                # if the value is smaller than the searchvalue we traverse on the right side of the tree
                return solution.searchBST(root.right, searchVal)
        

# Input: root = [4,2,7,1,3], val = 2
# Output: True 

#      4
#   2     7
# 1   3

solution = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(7)
result = []
print(solution.searchBST(root, 2))
print(solution.getBinaryTreeHeight(root))