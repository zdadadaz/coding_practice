# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
# O(NlogN)
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return (abs(left-right) <=1 and self.isBalanced(root.left) and self.isBalanced(root.right))
    
    def dfs(self,root):
        if not root:
            return 0
        return max(self.dfs(root.left),self.dfs(root.right))+1


# O(N)
    def isBalanced2(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.balance = True
        self.height(root)
        return self.balance
        
    def height(self,root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        if abs(left - right) >1:
            self.balance = False
            return -1
        return max(left,right)+1

