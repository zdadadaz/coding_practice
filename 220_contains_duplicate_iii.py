class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t<0 or k<=0:
            return False
        bucks = {}
        for i, val in enumerate(nums):
            idx = val//(t+1)
            if idx in bucks.keys():
                return True
            else:
                bucks[idx] = val
                if idx-1 in bucks.keys() and val - bucks[idx-1] <=t:
                    return True
                if idx+1 in bucks.keys() and bucks[idx+1] - val<=t:
                    return True
                if i>=k:
                    del bucks[nums[i-k]//(t+1)]
        return False
#         for i in range(len(nums)):
#             for j in range(i+1, i+1+k):
#                 if j < len(nums):
#                     if abs(nums[i]-nums[j])<=t:
#                         return True
#         return False
                    
        