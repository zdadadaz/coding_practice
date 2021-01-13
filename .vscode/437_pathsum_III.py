# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root==None:
            return 0
        return self.pathSum_recur(root,sum)+self.pathSum(root.left,sum)+self.pathSum(root.right,sum)
        
    def pathSum_recur(self,root, sum):
        if root == None:
            return 0
        res = 0
        if root.val == sum:
            res+=1
        res += self.pathSum_recur(root.left,sum-root.val)
        res += self.pathSum_recur(root.right,sum-root.val)
        return res
        