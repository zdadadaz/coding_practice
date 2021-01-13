# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        from collections import defaultdict
        self.cache = defaultdict(list)
        self.min = 0
        self.max = 0
        self.dfs(root, 0, 0) # root, row, col
        out = []
        for i in range(self.min,self.max+1):
            tmp = self.cache[i]
            tmp.sort()
            out.append([j[1] for j in tmp])
        return out
    
    def dfs(self,node,r,c):
        if node == None:
            return 
        self.dfs(node.left, r+1, c-1)
        self.dfs(node.right,r+1, c+1)
        self.cache[c].append((r,node.val))
        self.min = min(self.min, c)
        self.max = max(self.max, c)
        