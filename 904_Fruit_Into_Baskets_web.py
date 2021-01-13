class Solution(object):
    # sliding window
    # O(N)
    # O(1)
    # no hashmap
    def totalFruit(self, tree):
        res = 0
        left = 0
        right = -1
        n = len(tree)
        for i in range(1,n):
            if (tree[i] == tree[i - 1]):
                continue
            if (right >= 0 and tree[right] != tree[i]):
                res = max(res, i - left)
                left = right + 1
            right = i - 1
        return max(n - left, res)