class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s)==0:
            return 0
        from collections import defaultdict
        letters = defaultdict(int)
        for i in range(len(s)):
            letters[s[i]] += 1
        cnt = 0
        odd = 0
        for i in letters.keys():
            if letters[i]%2 == 1:
                odd = 1
            cnt+= (letters[i]//2)
        cnt *= 2
        return cnt+odd