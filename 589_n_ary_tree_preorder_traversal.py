"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.vis = []
        def dfs(root):
            if not root:
                return
            self.vis.append(root.val)
            for c in root.children:
                dfs(c)
        dfs(root)
        return self.vis


    def preorder_iteration(self, root: 'Node') -> List[int]:
        if not root:
            return []
        vis = []
        que = [root]
        while que:
            cur = que.pop()
            vis.append(cur.val)
            for i in cur.children[::-1]:
                que.append(i)
        return vis