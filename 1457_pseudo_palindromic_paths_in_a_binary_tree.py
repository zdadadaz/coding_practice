# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def dfs(root, acc):
            if not root:
                return 0
            acc ^= 1<<root.val
            res = dfs(root.left, acc) + dfs(root.right, acc)
            if root.left == root.right:
                if acc & (acc-1) == 0:
                    res += 1
            return res
        return dfs(root, 0)
            