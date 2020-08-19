class Solution:
    def titleToNumber(self, s: str) -> int:
        count = 0
        # for idx,i in enumerate(range(len(s)-1,-1,-1)):
        #     ch = ord(s[i]) - ord('A') +1
        #     if idx ==0:
        #         count += ch
        #     else:
        #         count += (26**idx)*ch
        # return count
        
        for i in s:
            ch = ord(i) - ord('A') +1
            count = count*26 + ch
        return count