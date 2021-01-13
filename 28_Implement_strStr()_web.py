class Solution:
    def strStr(self, haystack: str, needle: str):
        i = 0
        while i <= len(haystack) - len(needle):
            # use extract string is much faster than one letter to another
            if haystack[i:i+len(needle)] == needle:
                return i
            i += 1
        return -1