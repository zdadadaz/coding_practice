class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        res = ''
        i = N
        while i >0:
            if i & 1 == 1:
                res += '0'
            else:
                res += '1'
            i = i>>1
        res = res[::-1]
        return int(res,2)