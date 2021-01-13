class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        min1 = min2 = float('inf')
        for i in range(n):
            if nums[i]<=min1:
                min1 = nums[i]
            elif nums[i]<=min2:
                min2 = nums[i]
            else:
                return True
        return False                
                