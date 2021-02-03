class Solution:
    def strStr(self, haystack: str, needle: str):
        A= haystack
        B = needle
        if len(B) == 0:
            return 0
        if len(A) == 0 and len(B) == 0:
            return -1
        
        for i in range(len(A)):
            flag = True
            # use extract string is much faster than one letter to another
            for j in range(len(B)):
                if i+j>=len(A) or A[i+j] != B[j]:
                    flag = False
                    break
            if flag:
                return i
        return -1

    def strStr_2nd_mine(self, haystack: str, needle: str) -> int:
        n,m= len(haystack), len(needle)
        if n<m:
            return -1
        if m==0:
            return 0
        for i in range(n-m+1):
            if haystack[i:i+m]==needle:
                return i
            # flag = True
            # for j in range(m):
            #     if haystack[i+j]!=needle[j]:
            #         flag = False
            #         break
            # if flag:
            #     return i
        return -1