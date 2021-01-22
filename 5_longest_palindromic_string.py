class Solution:
    def longestPalindrome(self, s: str) -> str:
        st = end = 0
        maxlen = 0
        n = len(s)
        #odd
        for i in range(n-1):
            l = r = i
            while l>=0 and r <n:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            lenloc = r-l+1
            if lenloc > maxlen:
                maxlen = lenloc
                st = l+1
                end = r-1
        # even
        for i in range(n-1):
            l = i
            r = i+1
            while l>=0 and r <n:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            lenloc = r-l+1
            if lenloc > maxlen:
                maxlen = lenloc
                st = l+1
                end = r-1
        return s[st:end+1]

    # TLE: O(N^3) size loop is redundant. 
    def longestPalindrome_bruteforce(self, s: str) -> str:
        n = len(s)
        maxlen = 1
        st = end = 0
        for size in range(n):
            for i in range(n):
                l = i
                r = i+size
                # print('before',l,r)
                while r < n and l<=r and s[l]==s[r]:
                    l+=1
                    r-=1
                # print('after',l,r)
                if l>r:
                    if size+1 > maxlen:
                        maxlen = size+1
                        st = i
                        end = i+size
        if st ==0 and end == 0:
            return s[0]
        return s[st:end+1]