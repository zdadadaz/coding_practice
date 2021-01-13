class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<=1: return True
        lt = 0
        rt = len(s)-1
        while lt < rt:
            while lt < rt and not s[lt].isalnum(): lt += 1
            while lt < rt and not s[rt].isalnum(): rt -= 1
            if lt < rt and s[lt].lower() != s[rt].lower(): return False
            lt, rt =lt+1, rt-1
        return True

