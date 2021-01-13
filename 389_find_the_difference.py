class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = [0]*26
        for i in s:
            letters[ord(i)-ord('a')] +=1
        for i in t:
            letters[ord(i)-ord('a')] -=1
            if letters[ord(i)-ord('a')]<0:
                return i
        return ''