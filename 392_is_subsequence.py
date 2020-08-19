class Solution:
    def isSubsequence(self, s, t):
        sp = 0
        tp = 0
        while sp < len(s) and tp < len(t):
            # print(s[sp],)
            if s[sp] == t[tp]:
                sp+= 1
                tp+= 1
            else:
                tp+=1
        print(sp)
        if sp< len(s):
            return False
        else:
            return True
sol = Solution()
print(sol.isSubsequence("abc","ahbgdc"))