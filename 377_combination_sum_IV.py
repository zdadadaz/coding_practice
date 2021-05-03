class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        # important: dp[0] is one because dp[1] take from dp[0]
        dp[0] = 1
        for i in range(1,target+1):
            for j in nums:
                if i-j>=0:
                    dp[i] += dp[i-j]
        return dp[target]
        