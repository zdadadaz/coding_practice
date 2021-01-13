class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:(x[0],-x[1]))
        res = 0
        ending = 0
        
        for start, end in intervals:
            if end>ending:
                ending = end
                res +=1
        return res