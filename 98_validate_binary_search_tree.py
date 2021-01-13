# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(root, minV, maxV):
            if not root:
                return True
            if root.val <= minV or root.val >= maxV:
                return False
            validleft = dfs(root.left, minV, root.val)
            validright = dfs(root.right, root.val, maxV)
            return validleft and validright
        return dfs(root, float('-inf'), float('inf'))

            
        