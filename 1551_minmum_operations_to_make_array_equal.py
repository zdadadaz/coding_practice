class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        for i in range(n//2):
            a = (i*2)+1
            res += n-a
        return res