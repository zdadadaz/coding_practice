class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        def check(nums,positive):
            cnt = 0
            # positive = False # True: positive, False: negative
            for i in range(n-1):
                if not positive and nums[i] < nums[i+1]:
                    cnt += 1
                    positive = True
                elif positive and nums[i] > nums[i+1]:
                    cnt+=1 
                    positive = False
            return cnt+1          
        return max(check(nums,True), check(nums,False))

    def wiggleMaxLength_findpeakNvalley_(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        prv_diff = nums[1]- nums[0]
        cnt = 2 if prv_diff !=0 else 1
        for i in range(1, n):
            diff = nums[i] - nums[i-1]
            if (prv_diff<= 0 and diff>0) or  (prv_diff>=0 and diff < 0):
                cnt +=1 
                prv_diff = diff
        return cnt

