# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        count = [0]
        # self.dfs(root, count)
        # return count[0]
        # return self.dfs_m(root)
        return self.complete_tree_check(root)
    
    def dfs(self, node, count):
        if node.left != None:
            self.dfs(node.left, count)
        if node.right != None:
            self.dfs(node.right, count)
        count[0] += 1
    
#   while loop
    def dfs_m(self, node):
        queue = []
        queue.append(node)
        count = 0
        while len(queue) != 0:
            cur = queue.pop()
            count += 1
            if cur.left !=None:
                queue.append(cur.left)
            if cur.right !=None:
                queue.append(cur.right)
        return count
    
    def complete_tree_check(self, node):
        if node == None:
            return 0
        left_height = 1
        tmp_node = node
        while tmp_node.left:
            tmp_node = tmp_node.left
            left_height += 1
        right_height = 1
        tmp_node = node
        while tmp_node.right:
            tmp_node = tmp_node.right
            right_height += 1
            
        if left_height == right_height:
            return 2**left_height -1
        return (1+ self.complete_tree_check(node.left) + self.complete_tree_check(node.right))
        
            
        

sol = Solution()

print(sol.countNodes())