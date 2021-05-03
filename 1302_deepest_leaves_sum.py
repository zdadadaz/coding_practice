# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.tot = 0
        self.depth = 0
        def dfs(root, depth):
            if not root:
                return             
            if depth > self.depth:
                self.depth = depth
                self.tot = root.val
            elif depth == self.depth:
                self.tot+=root.val
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
            
        dfs(root, 1)
        return self.tot