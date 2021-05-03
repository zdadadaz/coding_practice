class Solution:
    def singleNumber_bit_manipulate(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res