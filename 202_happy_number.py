class Solution:
    def isHappy(self, n: int) -> bool:
        vis = set([1,7])
        while n>=10:
            tmp = n
            next_n = 0
            while tmp:
                next_n += (tmp%10)*(tmp%10)
                tmp = tmp//10
            if next_n in vis:
                return True
            vis.add(next_n)
            n = next_n
        if n in [1,7]:
            return True
        return False