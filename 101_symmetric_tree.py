# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(lt, rt):
            if not lt and not rt:
                return True
            if not lt or not rt:
                return False
            return lt.val == rt.val and \
                dfs(lt.left, rt.right) and \
                dfs(lt.right, rt.left)
        return dfs(root.left, root.right)