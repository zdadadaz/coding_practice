# two pointer question
# two condition
# no repeated word -> increase window (right++)
# repeated word, ex:'A' -> shrink window (left shift to the previous repeated word 'A')
# O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        maxL = 0
        visited = {}
        l = 0
        r = 0
        while r < len(s):
            # if visited and the position larger than left
            # if smaller than left means not connect to the current slide window(left,right)
            if s[r] in visited and visited[s[r]] >= l:
                l = visited[s[r]]
            # need to update position of traversed elements every time
            # Because it is for next left
            visited[s[r]] = r+1
            maxL = max(r-l+1,maxL)
            r+=1
        return maxL
    
    def lengthOfLongestSubstring_deletion(self, s: str) -> int:
        n = len(s)
        if n <2:
            return n
        hashset = {}
        lt= 0
        gLen = 0
        for rt in range(n):    
            if s[rt] in hashset:
                newlt = hashset[s[rt]]+1
                for i in range(lt, newlt):
                    del hashset[s[i]]
                lt = newlt    
            hashset[s[rt]] = rt
            gLen = max(gLen, rt-lt+1)
        return gLen



sol = Solution()
A = "abcabcbb"
sol.lengthOfLongestSubstring(A)