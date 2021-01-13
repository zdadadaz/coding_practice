class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            return [newInterval]
        if len(newInterval)==0:
            return intervals
        out = []
        newIn = newInterval
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            out.append(intervals[i])
            i+=1
        while i < n and intervals[i][0] <= newInterval[1]:
            newIn[0] = min(intervals[i][0], newIn[0])
            newIn[1] = max(intervals[i][1], newIn[1])
            i+=1
        out.append(newIn)
        while i < n and intervals[i][0] > newInterval[1]:
            out.append(intervals[i])
            i+=1
        return out
              