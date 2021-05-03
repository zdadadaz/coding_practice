# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = float('inf')
        def dfs(root, d):
            if not root:
                return 
            if not root.left and not root.right:
                self.res=min(self.res,d)
                return
            dfs(root.left, d+1)
            dfs(root.right,d+1)
        dfs(root,1)
        return self.res