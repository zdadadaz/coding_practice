# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def dfs(root, tot):
            if not root:
                return False
            tot -= root.val
            if tot==0 and not root.left and not root.right:
                return True
            
            return dfs(root.left, tot) or dfs(root.right, tot)
        return dfs(root,targetSum)