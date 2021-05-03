class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        half = len(nums)//2
        maxv = 0
        for i in c:
            if c[i]>half:
                return i
        return -1

    def majorityElement_voting(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        
        for i in nums:
            if count == 0:
                candidate = i
            count += 1 if candidate == i else -1
        return candidate