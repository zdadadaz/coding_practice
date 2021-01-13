"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        if len(intervals)==0:
            return 0
        n = len(intervals)
        line = []
        for i in range(n):
            line.append((intervals[i].start,1))
            line.append((intervals[i].end,-1))
        num, res = 0,0
        for _,x in sorted(line):
            num += x
            res = max(res, num)
        return res

    # heap solution
    def minMeetingRooms_heap(self, intervals):
        # Write your code here
        if len(intervals)==0:
            return 0
        n = len(intervals)
        from heapq import heappush, heappop
        intervals = sorted(intervals, key=lambda x: x.start)
        line = []
        heappush(line, intervals[0].end)
        for i in range(1,n):
            if intervals[i].start >= line[0]:
                heappop(line)
            heappush(line, intervals[i].end)
        return len(line)