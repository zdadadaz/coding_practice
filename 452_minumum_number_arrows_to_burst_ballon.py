class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: x[1])
        count = 0
        ending = float('-inf')
        for f,b in points:
            if f > ending:
                ending = b
                count += 1
        return count