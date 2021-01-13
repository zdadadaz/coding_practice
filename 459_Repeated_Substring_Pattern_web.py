class Solution:
    # Note:
    # assume there is no other letter not being repeated pattern, if repeated pattern in string.
    # ex: abcabcd  -> not exist because d is not supposed to exist.
    def repeatedSubstringPattern(self, s: str):
        N = len(s)
        # If there are repeated patterns in string,
        for i in range(1,int(N/2)+1):
            if N%i == 0:
                c = int(N/i)
                pattern = s[0:i] * c
                if pattern == s:
                    return True
        return False