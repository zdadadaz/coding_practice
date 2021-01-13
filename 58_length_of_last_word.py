class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s)==0:
            return 0
        count = 0
        for i in range(len(s)-1,-1,-1):
            char = s[i].lower()
            if ord(char) == ord(' ') and count!= 0:
                break
            elif ord(char) != ord(' '):
                count += 1
        return count