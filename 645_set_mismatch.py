class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = Counter(nums)
        dup = None
        idx = None
        for i in range(1,n+1):
            if i not in m:
                idx = i
                continue
            if m[i] == 2:
                dup = i
            if idx and dup:
                break
        return [dup,idx]
        