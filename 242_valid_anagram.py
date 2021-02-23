class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n!=m:
            return False
        from collections import Counter
        count_s = Counter(s)
        count_t = Counter(t)
        return count_s == count_t