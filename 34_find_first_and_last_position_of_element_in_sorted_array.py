class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1,-1]
        
        def BS(nums):
            l = 0
            r = n-1
            minidx = n
            while l < r:
                mid = (r+l)//2
                if target==nums[mid]:
                    minidx = min(minidx, mid)
                # tend to find minimum index
                if target <= nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            if target == nums[l]:
                minidx = min(minidx, l)
            return minidx if minidx!=n else -1
        
        def BSmax(nums):
            l = 0
            r = n-1
            maxidx = -1
            while l < r:
                mid = (r+l)//2
                if target==nums[mid]:
                    maxidx = max(maxidx, mid)
                # tend to find maximum index
                if target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            if target == nums[l]:
                maxidx = max(maxidx, l)
            return maxidx
        
        return [BS(nums), BSmax(nums)]


    def searchRange_lean_code(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        if N == 0:
            return [-1,-1]
        
        st, end = -1, -1
        l,r = 0, N
        # binary search left
        while l < r:
            mid = (l+r)//2
            if nums[mid]>=target:
                r = mid
            else:
                l = mid+1
        if l<N and nums[l]==target:
            st = l
        
        l,r = 0, N
        while l < r:
            mid = (l+r)//2
            if nums[mid]<=target:
                l = mid+1
            else:
                r = mid
        if nums[r-1]==target:
            end = r-1
        return [st, end]