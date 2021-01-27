class Solution:
    def concatenatedBinary(self, n: int) -> int:
        modulo = 10**9 + 7
        val = 0
        for i in range(1,n+1):
            tmp = i
            while tmp>0:
                val <<=1
                tmp  >>= 1
            val += i
            val %= modulo
        return val

    def concatenatedBinary_and_or(self, n: int) -> int:
        modulo = 10**9 + 7
        val = 0
        length = 0
        for i in range(1,n+1):
            if i & (i-1)==0:
                length +=1
            val = ((val<<length)|i)%modulo
        return val



