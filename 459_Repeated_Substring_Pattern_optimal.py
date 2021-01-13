class Solution:
    # Note:
    # assume there is no other letter not being repeated pattern, if repeated pattern in string.
    # ex: abcabcd  -> not exist because d is not supposed to exist.
    
    # repeat the string once and cut off head and tail string
    # check if s in newly created string
    
    # goal: it is like creating a mirror to reflect the repeated pattern
    #       in the string

    # Only can check whether there is repeated pattern
    # can not know what is the pattern
    def repeatedSubstringPattern(self, s: str):
        N = len(s)
        ss = s*2
        ss = ss[1:-1]
        if s in ss:
            return True
        return False