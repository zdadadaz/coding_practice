class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # while(val in nums):
        #     del nums[nums.index(val)]
        # return len(nums)
        lt = 0
        rt = len(nums)
        while lt < rt:
            if nums[lt] == val:
                nums[lt] = nums[rt-1]
                rt -= 1
            else:
                lt += 1
        return lt