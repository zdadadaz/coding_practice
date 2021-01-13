# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST_BFS(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        from collections import deque
        que = deque()
        que.append(root)
        while que:
            cur = que.pop()
            if cur.val == val:
                return cur
            elif val < cur.val and cur.left:
                que.append(cur.left)
            elif val > cur.val and cur.right:
                que.append(cur.right)
        return None
    def searchBST_DFS(self, root: TreeNode, val: int) -> TreeNode:
        # DFS
        if not root:
            return None
        while root:
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right
        return None
    def searchBST_Recursion(self, root: TreeNode, val: int) -> TreeNode:
        # Recursion
        if not root is None:
            return None
        if root.val == val:
            return root
        elif val <= root.val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)
            
        