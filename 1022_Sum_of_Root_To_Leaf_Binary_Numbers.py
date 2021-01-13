# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, '')
        return self.res
    def dfs(self,root, binary):
        if root == None:
            return 
        binary += str(root.val)
        if root.left == None and root.right == None and len(binary)!= 0:
            self.res+=int(binary, 2)
            return
        self.dfs(root.left, binary)
        self.dfs(root.right, binary)

