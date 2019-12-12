# 395. Longest Substring with At Least K Repeating Characters
# use count to record number of repeated character
# while loop to reduce one character at one time from left pointer.
class Solution:
    def lengthOfLongestSubstring(self, s: str,k):
        r = 0
        l = 0
        count = [0]*26
        maxL = 0
        N = len(s)
        u=0
        for i in range(N):
            if count[ord(s[i]) - ord('a')]==0:
                u += 1
            count[ord(s[i]) - ord('a')] += 1

        if u < k:
            print("Not enough unique character")
            return -1
        
        count = [0]*26
        r = 0
        l = 0
        while r < N:
            count[ord(s[r]) - ord('a')] += 1
            # check number of distinct is less than k
            # not move l += 1
            while not self.isValid(count,k):
                count[ord(s[r]) - ord('a')] -= 1
                l += 1
            
            maxL = max(maxL, r-l+1)
            r+=1

        return maxL

    def isValid(self,count,k):
        tmp = 0
        for i in range(len(count)):
            if count[i]>0:
                tmp+= 1
        return tmp <= k
        
sol = Solution()
A = "aabacbebebe"
qq = sol.lengthOfLongestSubstring(A,2)
print(qq)