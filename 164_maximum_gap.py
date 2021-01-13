class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2:
            return 0
        minV = min(nums)
        maxV = max(nums)
        if maxV == minV:
            return 0
        interval = ceil((maxV-minV)/(n-1))
        bnum = (maxV-minV)//interval+1
        buckets = [[None, None] for i in range(bnum)]
        for num in nums:
            bucket_id = (num-minV)//interval
            bucket = buckets[bucket_id]
            bucket[0] = min(bucket[0], num) if bucket[0] else num
            bucket[1] = max(bucket[1], num) if bucket[1] else num
        buckets = [b for b in buckets if b[0]]
        return max(buckets[i][0]-buckets[i-1][1] for i in range(1, len(buckets)))
            