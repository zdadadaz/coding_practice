class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        bit =[0]*32
        i = 0
        while n > 0:
            bit[i] = n&1
            n = n>>1
            i+=1
        base = 1
        for i in bit[::-1]:
            res += base*i
            base = base<<1
        return res

    def reverseBits_no_extraMemory(self, n: int) -> int:
        res = 0
        power = 31
        while n>0:
            res += (n&1)<<power
            power -= 1
            n = n>>1
        return res


