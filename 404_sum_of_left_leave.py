# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.acc = 0
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.dfs(root,False)
        return self.acc
    
    def dfs(self,root,isLeft):
        if isLeft and root.left == None and root.right == None:
            self.acc += root.val
            return 
        if root.left != None:
            self.dfs(root.left,True)
        if root.right != None:
            self.dfs(root.right,False)

    def sumOfLeftLeaves_mine(self, root: TreeNode) -> int:
        if root == None:
            return 0
        acc = 0
        if root.left != None:
            if root.left.left == None and root.left.right == None:
                acc+= root.left.val
            acc += self.sumOfLeftLeaves(root.left)
        if root.right != None:
            acc += self.sumOfLeftLeaves(root.right)
        
        return acc
