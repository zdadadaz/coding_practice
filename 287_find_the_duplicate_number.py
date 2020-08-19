class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return []
        n = len(nums)
        max_idx = max_num = 0
        for i in range(len(nums)):
            tmp_idx = nums[i]%n
            nums[tmp_idx] += n
            if nums[tmp_idx] > max_num:
                max_idx = tmp_idx
                max_num = nums[tmp_idx]
        return max_idx
    