class Solution:
    def missingNumber_bit(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

    def missingNumber_sum(self, nums: List[int]) -> int:
        n = len(nums)
        tot = (n+1)*n/2
        for i in nums:
            tot -= i
        return int(tot)