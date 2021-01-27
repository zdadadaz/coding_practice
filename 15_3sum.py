class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n-2):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            l = i+1
            r = n-1
            while l < r:
                sumtmp = nums[i] + nums[l] + nums[r]
                if sumtmp<0:
                    l+=1
                elif sumtmp > 0:
                    r-=1
                else:
                    res.append([nums[i],nums[l] ,nums[r]])
                    while l < n-1 and nums[l+1] == nums[l]: l+=1
                    while r >0 and nums[r] == nums[r-1]: r-=1 
                    l+=1
                    r-=1
        return res