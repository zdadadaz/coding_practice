class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        overlap = [intervals[0][0],intervals[0][1]]
        res = []
        for i in range(1,n):
            if intervals[i][0] <= overlap[1]:
                overlap[0] = min(overlap[0], intervals[i][0])
                overlap[1] = max(overlap[1], intervals[i][1])
            else:
                res.append([overlap[0],overlap[1]])
                overlap[0] = intervals[i][0]
                overlap[1] = intervals[i][1]
        res.append([overlap[0],overlap[1]])
        return res
                