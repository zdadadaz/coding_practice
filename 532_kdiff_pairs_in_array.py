class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        dictn = defaultdict(int)
        for i in nums:
            dictn[i] += 1
        res = set()
        for i in nums:
            diff = k+i
            if (diff != i and dictn[diff] != 0) or (diff==i and dictn[diff] >1):
                if i > diff:
                    res.add((i,diff))
                else:
                    res.add((diff,i))
        return len(res)
            