# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if root == None:
            return ''
        self.lst=[]
        def dfs(node):
            if not node: return 
            self.lst.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(map(str,self.lst))
        
    def deserialize(self, data: str) -> TreeNode:
        if len(data)==0:
            return None
        lst = [int(i) for i in data.split(',')]
        
        def rec(lst, lower, upper):
            if not lst: return None
            if not lower <= lst[0] <= upper: return None
            cand = lst.pop(0)
            root = TreeNode(cand)
            root.left = rec(lst, lower, root.val)
            root.right = rec(lst, root.val, upper)
            return root
        return rec(lst, -float('inf'), float('inf'))
            

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans