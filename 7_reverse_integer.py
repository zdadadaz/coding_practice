class Solution:
    def reverse(self, x: int) -> int:
        intmax = 2**31
        sign = -1 if x<0 else 1
        res = 0
        x = abs(x)
        while x != 0:
            res = res *10 + x%10
            if res >=intmax:
                return 0
            x = x // 10
        return res*sign