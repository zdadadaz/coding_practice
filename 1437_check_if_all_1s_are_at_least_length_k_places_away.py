class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prv_idx = -1
        for i in range(n):
            if prv_idx == -1 and nums[i] == 1:
                prv_idx = i
            elif nums[i] == 1:
                dist = i-prv_idx-1
                if dist < k:
                    return False
                prv_idx = i
        return True
    
    def kLengthApart_bit_manipulate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        num = 0
        for i in nums:
            num = (num + i)<<1
        if num == 0:
            return True
        while num & 1 == 0:
            num = num >>1        
        prv = 0
        cnt = 1
        num >>=1
        while num > 0:
            if num&1 == 1:
                if cnt - prv - 1 < k:
                    return False            
                prv = cnt
            cnt += 1
            num >>= 1
        return True
            