class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 1
        cnt = 0
        for i in range(1,n+1):
            res = res*i
        while res>9:
            if res %10 == 0:
                cnt +=1
            else:
                break
            res = res // 10
        return cnt

    def trailingZeroes_numof5(self, n: int) -> int:
        cnt = 0
        for i in range(1,n+1):
            tmp = i
            while tmp % 5 == 0:
                cnt +=1
                tmp = tmp // 5
        return cnt

