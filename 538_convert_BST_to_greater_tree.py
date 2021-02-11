# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return 
        self.helper(root, 0)
        return root
    
    def helper(self, root, val):
        if not root:
            return val
        root.val = root.val + self.helper(root.right, val) 
        val = self.helper(root.left, root.val)
        return val