class Solution:
    def findLHS_hashmap(self, nums: List[int]) -> int:
        n = len(nums)
        from collections import defaultdict
        m = defaultdict(int)
        for i in nums:
            m[i] += 1
        
        maxlen = 0
        for i in m.keys():
            if i+1 in m:
                maxlen = max(maxlen, m[i]+m[i+1])
        return maxlen
            

    def findLHS_hashmap_singleloop(self, nums: List[int]) -> int:
        n = len(nums)
        from collections import defaultdict
        m = defaultdict(int)
        
        maxlen = 0
        for i in nums:
            m[i] += 1
            if i-1 in m:
                maxlen = max(maxlen, m[i]+m[i-1])
            if i+1 in m:
                maxlen = max(maxlen, m[i]+m[i+1])
        return maxlen
            
                        