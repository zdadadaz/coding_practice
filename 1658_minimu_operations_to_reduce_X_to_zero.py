class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return n
        lt = 0
        n_target = -1
        sub_sum = 0
        for rt in range(n):
            sub_sum += nums[rt]
            while sub_sum > target:
                sub_sum -= nums[lt]
                lt += 1
            if sub_sum == target:
                n_target = max(n_target, rt-lt+1)
        return n-n_target if n_target != -1 else -1
    

    def minOperations_hashmap(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return n
        dictsum = {}
        sub_sum = 0
        for i in range(n):
            sub_sum += nums[i]
            dictsum[sub_sum] = i
        dictsum[0] = -1
        sub_sum = 0
        res = -1
        for i in range(n):
            sub_sum += nums[i]
            if (sub_sum - target) in dictsum:
                res = max(res, i - dictsum[sub_sum - target])
        return n-res if res >0  else -1 
                    
    