class Solution:
    def shortestPalindrome(self, s: str):
        revStr = s[::-1] 
        # Get concatenation of string,  
        # special character and reverse string  
        concat = s + "$" + revStr  
        lps = self.computeLPSArray(concat)
        rev = s[lps[-1]:]
        
        return rev[::-1]+s
    
    def computeLPSArray(self,s):
        i = 1
        length = 0
        N = len(s)
        lps = [None] * N
        lps[0] = 0
        while i < N:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i+=1
        return lps