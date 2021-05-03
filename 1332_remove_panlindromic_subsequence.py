class Solution:
    def removePalindromeSub(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        for i in range(n//2):
            if s[i] != s[n-1-i]:
                return 2
        return 1