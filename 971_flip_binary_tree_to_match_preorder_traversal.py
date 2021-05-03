# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        if root.val != voyage[0]:
            return [-1]
        self.idx = 0
        self.vis = []
        def dfs(root):
            if not root or self.idx == len(voyage):
                return 
            if root.val != voyage[self.idx]:
                self.vis.append(None)
                return 
            self.idx += 1
            if root.left and root.right and root.left.val != voyage[self.idx]:
                self.vis.append(root.val)
                root.left, root.right = root.right, root.left            
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        if None in self.vis:
            return [-1]
        return self.vis