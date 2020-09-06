# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return root
        def predecessor(root):
            while root.right != None:
                root = root.right
            return root.val
        def successor(root):
            while root.left != None:
                root = root.left
            return root.val
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # leaf
            if root.left == None and root.right ==None:
                root =None
            # have left
            elif root.left != None:
                root.val = predecessor(root.left)
                root.left = self.deleteNode(root.left, root.val)
            else:
                root.val = successor(root.right)
                root.right = self.deleteNode(root.right, root.val)
        return root