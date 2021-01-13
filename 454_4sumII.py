class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        from collections import defaultdict
        map = defaultdict(int)
        for i in A:
            for j in B:
                if i+j in map:
                    map[(i+j)] += 1
                else:
                    map[(i+j)] = 1
        cnt = 0
        for i in C:
            for j in D:
                if -(i+j) in map:
                    cnt += map[-(i+j)]
        return cnt
        