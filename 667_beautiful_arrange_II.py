class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = [i for i in range(1,n-k+1)]
        diff = k
        dr = 1
        for i in range(k):
            res.append(res[-1]+diff*dr)
            dr *= -1
            diff -= 1
        return res

