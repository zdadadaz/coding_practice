class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        dp = {}
        module = 10**9+7
        for i in range(n):
            dp[arr[i]] = 1
            for j in range(0,i):
                left = arr[i]%arr[j]
                divid = arr[i]//arr[j]
                if left == 0 and divid in dp:
                    dp[arr[i]] += ((dp[divid] * dp[arr[j]])%module)
        res = 0
        for i in dp:
            res += dp[i]
        return res%module