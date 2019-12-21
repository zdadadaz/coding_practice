# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.
# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

# Example 1:
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.

# Example 2:
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

from pythonds.basic import Stack
class Solution():
    # time = HH:MM
    def __init__(self):
        self.digits = None

    def next_closest_time(self,time):
        df_stack = Stack()
        visited = set()
        digits = []
        for i in time:
            if i != ':':
                digits.append(i)
        givenTime = []
        self.digits = []
        for i in digits:
            givenTime.append(int(i))
            if i not in self.digits:
                self.digits.append(i)
        init = [0]*4
        minTime = [24*60]
        timeStamp = ['']
        visited.add(str(givenTime))
        self.dfs(0, init,visited,givenTime,minTime,timeStamp)
        return timeStamp[0]
        
    def dfs(self, depth, cur, visited, givenTime, minTime,timeStamp):
        if depth == 4:
            if str(cur) in visited:
                return
            visited.add(str(cur))
            time_diff = self.time_difference(cur, givenTime)
            if self.isValid(cur) and time_diff < minTime[0]: #minTime:
                minTime[0] = time_diff
                timeStamp[0] = str(cur[0]) + str(cur[1]) + ":" + str(cur[2]) + str(cur[3])
            return

        for i in self.digits:
            cur[depth] = int(i)
            self.dfs(depth+1, cur, visited, givenTime, minTime,timeStamp)
        
    def time_difference(self, time1, time2):
        t1 = self.to_minutes(time1)
        t2 = self.to_minutes(time2)
        aday = 24*60
        return (t1-t2 + aday) % aday

    def to_minutes(self,time):
        hh = time[0]*10 + time[1]
        mm = time[2]*10 + time[3]
        return hh*60 + mm

    def isValid(self, time):
        hh = time[0]*10 + time[1]
        mm = time[2]*10 + time[3]
        if hh > 23 or mm>59:
            return False
        return True
            

aa = '19:34'
bb = '23:59'
sol = Solution()
print(sol.next_closest_time(bb))