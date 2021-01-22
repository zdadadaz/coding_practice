class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        from collections import defaultdict
        m = defaultdict(int)
        for i in nums:
            if i in m and m[i]>0:
                cnt += 1
                m[i] = m[i]-1 if m[i]>0 else 0
            elif i < k:
                m[k-i] += 1
        return cnt
                