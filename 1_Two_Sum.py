import numpy as np
class Solution:
    # O(nlogn)
    def twoSum(self, nums: List[int], target: int):
        array = np.array(nums)
        ind = np.argsort(array)
        i=0
        j=len(nums)-1
        while i<j:
            if nums[ind[i]]+nums[ind[j]] == target:
                return [ind[i],ind[j]]
            elif nums[ind[i]]+nums[ind[j]] > target:
                j-=1
            else:
                i+=1
        return -1

    # hash method
    def twoSum_hash_N(self, nums: List[int], target: int):
        record = {}
        for i in range(len(nums)):
            if nums[i] not in record.keys():
                record[target - nums[i]] = i
            else:
                return [record[nums[i]], i]
        return -1