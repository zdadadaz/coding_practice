class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        import heapq
        n = len(nums)
        vmin = float('inf')
        for i in range(n):
            if nums[i] % 2 == 1:
                nums[i] *= 2
            vmin = min(nums[i], vmin)
            nums[i] *= (-1)
            
        heapq.heapify(nums)
        res = float('inf')
        while nums[0]%2 == 0:
            cur = heapq.heappop(nums)
            heapq.heappush(nums,cur//2)
            vmin = min(vmin, -cur//2)
            res = min(res, -nums[0] - vmin)
        return res