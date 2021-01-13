# naive approach
# time out
class Solution:
    def shortestPalindrome(self, s: str):
        n = len(s)
        for i in range(n-1,-1,-1):
            if self.isPanlindrome(i,s):
                rev = s[(i+1):]
                rev = rev[len(rev)::-1]
                return rev+s
        
        rev = s[1:]
        rev = rev[len(rev)::-1]
        return rev+s
    
    def isPanlindrome(self,index,s):
        st = 0
        end = index
        while st <=end:
            if s[st] == s[end]:
                st+=1
                end-=1
            else:
                return False
        return True