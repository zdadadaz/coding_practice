# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def recur(root, res):
            if not root:
                return 
            recur(root.left, res)
            res.append(root.val)
            recur(root.right, res)
            return res
        res = recur(root,[])
        head = TreeNode(res[0])
        cur = head
        for i in res[1:]:
            cur.right = TreeNode(i)
            cur = cur.right
        return head