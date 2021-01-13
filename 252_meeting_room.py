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
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        intervals.sort(key=lambda x: (x.start, x.end))
        if len(intervals)==0:
            return True
        n = len(intervals)
        for i in range(1, n):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True