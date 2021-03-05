class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        for i in range(1, 2**31):
            num = i**2
            if num> x:
                return i-1
            elif num == x:
                return i
        return -1

    # O(log(N/2))
    def mySqrt_BST(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        l,r = 1, x//2
        while l <= r : # 6 [1,3]
            mid = (l+r)//2
            num = mid**2
            if num == x:
                return mid
            elif num< x:
                l = mid+1
            else:
                r = mid-1
        return r
        