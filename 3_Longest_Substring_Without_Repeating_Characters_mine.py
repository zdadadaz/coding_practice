# O(n^2)
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        out = ''
        maxL = 0
        for i in range(len(s)):
            visited = set()
            count = 0
            for j in range(i,len(s)):
                if s[j] not in visited:
                    visited.add(s[j])
                    out += s[j]
                    count +=1
                else:
                    break
            if count>maxL:
                maxL = count
        return maxL
        