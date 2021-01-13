class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A)!= len(B):
            return False
        if A==B and len(set(A))<len(A):
            return True
        diff = []
        for i in range(len(A)):
            if A[i]!=B[i]:
                diff.append([A[i], B[i]])
        
        if len(diff)==2 and diff[0] == diff[-1][::-1]:
            return True
        return False