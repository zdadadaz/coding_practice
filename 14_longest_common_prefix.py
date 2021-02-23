class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ''
        l = 0
        res = []
        while 1:
            if len(strs[0])==0:
                return ''.join(res)
            for i in range(0,n):
                if l>= len(strs[i]) or strs[0][l] != strs[i][l]:
                    return ''.join(res)
            res.append(strs[0][l])
            l+=1
        return ''