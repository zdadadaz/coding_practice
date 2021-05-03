# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def dfs(root, depth, prv_left):
            if depth == d:
                if prv_left:
                    return TreeNode(v, root, None)
                else:
                    return TreeNode(v, None, root)
            if not root:
                return None
            
            root.left = dfs(root.left, depth+1, True)
            root.right = dfs(root.right, depth+1, False)
            return root
        return dfs(root, 1, True)