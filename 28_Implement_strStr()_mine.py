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