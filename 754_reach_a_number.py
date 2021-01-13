class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        sumk = 0
        for i in range(target+1):
            sumk+=i
            if sumk >= target:
                k = i
                break
        d = sumk - target
        if d % 2 == 0:
            return k
        return k + 1 + (k%2)
            