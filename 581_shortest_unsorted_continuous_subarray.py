class Solution:
    # Sorted O(nlogn)
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        num2 = sorted(nums)
        l, r= n, float('-inf')
        for i in range(n):
            if num2[i]!= nums[i]:
                l = min(l,i)
                r = max(r,i)
        if l!=n:
            return r-l+1
        return 0

    # Stack O(N)
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        # [2,6,4,8,10,9,15]
        stack = []
        #(i,num)
        l,mx = n, float('-inf')
        for i,num in enumerate(nums):
            while stack and stack[-1][1] > num:
                cond = stack.pop()
                l = min(l, cond[0])
                mx = max(mx, cond[1])
            stack.append((i,num))
        if l == n:
            return 0
        r = -1
        for i in range(n-1,-1,-1):
            if nums[i]<mx:
                r = i
                break
        return r-l+1
                

