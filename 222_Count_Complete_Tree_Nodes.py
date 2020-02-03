class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        count = [0]
        self.dfs(root, count)
        return count[0] 
    
    def dfs(self, node, count):
        if node.left != None:
            self.dfs(node.left, count)
        if node.right != None:
            self.dfs(node.right, count)
        count[0] += 1

sol = Solution()

print(sol.countNodes())