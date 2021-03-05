class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cur = 0
        res = float('-inf')
        # dont need to add another minus number
        # [-2,1,-3,4,-1,2,1,-5,4]
        for i in nums:
            if cur < 0:
                cur = i
            else:
                cur += i
            res = max(cur, res)
        return res