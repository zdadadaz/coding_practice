class Solution:
    def countPrimes(self, n: int) -> int:
        if n <2:
            return 0
        res = [True for i in range( n)]
        res[0], res[1] = False, False
        half = int(sqrt(n))
        for i in range(2,half+1):
            if res[i]:
                square = i*i
                for j in range(n):
                    tmp = square + j*i
                    if tmp < n:
                        res[tmp] = False
                    else:
                        break
        return sum(res)
            