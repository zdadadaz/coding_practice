class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <=0:
            return False
        while n>1:
            if int(n%3) == 0:
                n = n/3
            else:
                return False
        return True

    def isPowerOfThree_log(self, n: int) -> bool:
        if n<= 0:
            return False
        import math
        return round(math.log(n,3),10)%1 == 0