# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return 0
        res = []
        que = [root]
        while que:
            tot = 0
            cnt = 0
            for _ in range(len(que)):
                cur = que.pop(0)
                tot += cur.val
                cnt += 1
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            res.append(tot/cnt)
        return res
                