class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = 0
        f = 0
        n = len(nums)
        # while f < n:
        #     if nums[f] == nums[s]:
        #         f+=1
        #     else:
        #         s+=1
        #         nums[f],nums[s] = nums[s],nums[f] 
        #         f+=1
        # return s+1
        
        for f in range(1, n):
            if nums[f] != nums[s]:
                s +=1
                nums[s] = nums[f]
        return s+1
            