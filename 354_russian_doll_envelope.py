class Solution:
    # TLE
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        dp = [1]*n
        envelopes.sort(key = lambda k:(k[0],-k[1]) )
        for i in range(n):
            cur = envelopes[i]
            for j in range(i):
                tmp = envelopes[j]
                if tmp[0] < cur[0] and tmp[1] < cur[1]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

    # after ascend width and descend height, always compare height, replace when height <= dp[i]
    def maxEnvelopes_sort2way(self, envelopes: List[List[int]]) -> int:
        dp = []
        envelopes.sort(key = lambda k:(k[0],-k[1]) )
        for w,h in envelopes:
            i,N = 0,len(dp)
            while i < N:
                if h<=dp[i]:
                    break
                i+=1
            if i == N:
                dp.append(h)
            else:
                dp[i] = h
        return len(dp)

    def maxEnvelopes_bisect(self, envelopes: List[List[int]]) -> int:
        dp = []
        envelopes.sort(key = lambda k:(k[0],-k[1]) )
        for w,h in envelopes:
            i = bisect_left(dp,h)
            if i == len(dp):
                dp.append(h)
            else:
                dp[i] = h
        return len(dp)