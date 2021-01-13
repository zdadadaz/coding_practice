class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        slen = len(s)
        for i in range(1,slen//2+1):
            tmp = s[:i]
            if tmp*(slen//i)==s:
                return True
        return False

    def repeatedSubstringPattern_v2(self, s: str) -> bool:
        if len(s)<1:
            return False
        ss = (s+s)[1:-1]
        return ss.find(s)!=-1
        
            
            