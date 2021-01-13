class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        prod = 1
        res = 0
        for r in range(len(nums)):
            prod *= nums[r]
            if prod >= k:
                while prod >=k and l <=r:
                    prod /= nums[l]
                    l+=1
            res +=r-l+1
        return res
        
    def logn2_sol(self, nums, k):
        n = len(nums)
        res_num = 0
        for i in range(n):
            prod = nums[i]
            if prod <k:
                res_num+=1
            else:
                continue
            for j in range(i+1, n):
                prod *= nums[j]
                if prod <k:
                    res_num+=1
                else:
                    break
        return res_num