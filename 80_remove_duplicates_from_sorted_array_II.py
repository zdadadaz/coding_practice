class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<3:
            return len(nums)
        s= 2
        n= len(nums)
        for f in range(2,n):
            if nums[f]!=nums[s-1] or nums[f]!=nums[s-2]:
                if s!=f:
                    nums[s] = nums[f]
                s+=1
        return s

