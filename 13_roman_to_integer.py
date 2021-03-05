class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)-1
        res = 0
        m = {'I':1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M': 1000}
        prv = -1
        while n >= 0:
            cur = m[s[n]]
            if cur >= prv:
                res += cur
            else:
                res -= cur
            prv = cur
            n-=1
        return res